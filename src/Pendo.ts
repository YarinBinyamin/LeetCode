type F = (x: number) => number;

function compose(functions: F[]): F {
    if (functions.length === 0){
        return (number) => number;
    }

    return function(x) {
      const ans = functions.reduceRight((acc,fi) => fi(acc), x);
      return ans
    }

};