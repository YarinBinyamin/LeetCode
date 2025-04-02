class Solution(object):
    def climbStairs(self, n: int) -> int:
        ans_dp = [0] * (n + 1)
        ans_dp[0] = 1
        ans_dp[1] =1
        for i in range(2 , n +1, 1):
            ans_dp[i] = ans_dp[i-1] + ans_dp[i-2]
        return ans_dp[n]
    
class Solution:
    def simplifyPath(self, path: str) -> str:
        if path.index(size(path)-1) == '/':
           path = path[:-1]
        start = 0
        for i in range(1,size(path) -1, +1):
            if path.index(i).isalpha():
                continue
            if path.index(i) == '.':
                start = 1
                    
    
if __name__ == "__main__":
    sol = Solution()
    result = sol.climbStairs(10)
    print("Result:", result)