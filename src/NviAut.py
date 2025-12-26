from dataclasses import dataclass
import subprocess
import pytest
from typing import List,Optional
import time
from typing import Callable, TypeVar
@dataclass
class CmdResult:
    cmd: List[str]
    rc: int
    out: str
    err: str
    TimeoutError: bool=False
    
class CommandError(RuntimeError):
    def __init__(self, result: CmdResult):
        super().__init__(
            f"Command failed (rc={result.rc}): {' '.join(result.cmd)}\n"
            f"stderr:\n{result.err}"
        )
        self.result = result
    
def run_cmd(cmd: List[str], timeout: int =10, check: bool =False) -> CmdResult:
    try:
        p = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=timeout
        )
        result = CmdResult(cmd=cmd, rc=p.returncode, out=p.stdout.strip(), err=p.stderr.strip())

        if check and result.rc != 0:
            raise CommandError(result)

        return result

    except subprocess.TimeoutExpired as e:
        # Note: TimeoutExpired may have partial stdout/stderr
        out = (e.stdout or "")
        err = (e.stderr or "")
        return CmdResult(cmd=cmd, rc=124, out=out, err=err, timeout=True)
    
def test_check_true_raises():
    res = run_cmd(["python", "5", "ptrint('hi')"])
    assert res.rc !=0 , pytest.raises(CommandError)

class Runner(Protocol):
    def run(self, cmd: List[str], timeout: int = 10) -> CmdResult:
        ...


# 3) LocalRunner is the actual implementation that uses subprocess
class LocalRunner:
    def run(self, cmd: List[str], timeout: int = 10) -> CmdResult:
        try:
            p = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
            return CmdResult(
                cmd=cmd,
                rc=p.returncode,
                out=p.stdout.strip(),
                err=p.stderr.strip(),
                timeout=False
            )
        except subprocess.TimeoutExpired as e:
            return CmdResult(
                cmd=cmd,
                rc=124,
                out=(e.stdout or "").strip(),
                err=(e.stderr or "").strip(),
                timeout=True
            )


# 4) Device has behavior -> normal class (not dataclass) is simplest
class Device:
    def __init__(self, name: str, runner: Runner):
        self.name = name
        self.runner = runner

    def run(self, cmd: List[str], timeout: int = 10, check: bool = False) -> CmdResult:
        res = self.runner.run(cmd, timeout=timeout)

        # log failures/timeouts (useful for CI)
        if res.timeout:
            print(f"[{self.name}] TIMEOUT cmd={' '.join(cmd)}")
        elif res.rc != 0:
            print(f"[{self.name}] FAIL rc={res.rc} cmd={' '.join(cmd)}")

        # optionally raise
        if check and (res.timeout or res.rc != 0):
            raise CommandError(res)

        return res


def assert_ok(res: CmdResult) -> None:
    if res.timeout:
        raise AssertionError("timed out ...")
    elif res.rc != 0:
        AssertionError(res.rc, res.cmd,res.out.strip(), res.err.strip())
        
        
def test_check_true_raises_includes_result():
    with bytes.raises(CommandError) as excinfo:
        run_cmd([sys.executable, "-c", "import sys; sys.exit(2)"], check=True)

    err_obj = excinfo.value
    assert err_obj.result.rc == 2
    
T = TypeVar("T")

def wait_until(fn: Callable[[], T], predicate: Callable[[T], bool],timeout: float = 5.0, interval: float = 0.2) -> T:
    """
    Calls fn repeatedly until predicate(result) is True or timeout expires.
    Returns the last result if successful, otherwise raises TimeoutError.
    """
    endTime = time.time() + timeout
    while time.time() < endTime :
        res = fn()
        last = res
        if predicate(res):
            return res
        time.sleep(interval)
    raise TimeoutError(f"Condition not met within {timeout} seconds. Last result: {last}")
         
    
@pytest.fixture
def dut():
    return Device("DUT1", LocalRunner())
def test_vlan_output(dut):
    return  dut.run(["show", "vlan"])

@pytest.mark.parametrize("vlan_id", [1, 100, 200])
def test_vlan_id_exist(dut, vlan_id):
    res = test_vlan_output(dut)
    vlans = res["vlans_id"]
    assert vlan_id in vlans
    
        
            
if __name__ == "__main__":
    dev = Device("LOCAL", LocalRunner())
    res = dev.run(["python", "-c", "print('hi')"], check=True)
    print("stdout:", res.out)