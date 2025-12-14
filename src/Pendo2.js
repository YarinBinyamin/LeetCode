const { Interface } = require("readline");

var isSumEqual = function(firstWord, secondWord, targetWord) {
    const covertor = (a) => (a.charCodeAt(0) - 'a'.charCodeAt(0)) 
    const wordToNum = (word) => {
        const strVal = Array.from(word).reduce((acc, x) => acc + covertor(x), "")
        return Number(strVal);
    }
    const left = wordToNum(firstWord) + wordToNum(secondWord)
    const right = wordToNum(targetWord)
    return left === right 
};

var countMatches = function(items, ruleKey, ruleValue) {
    const rules = ["type","color","name"]
    const indexRuleKey = rules.indexOf(ruleKey)
    return items.filter(item => item[indexRuleKey] === ruleValue).length
    
};
var decrypt = function(code, k) {
    const n = code.length
    const arr = new Array(n).fill(0)
    if (k == 0 ){
        return arr
    } 
    const extended = code.concat(code)
    return code.map((value,index) =>{
        let sum = 0 
        if(k>0){
            const start = index +1 
            const end = index +1+k 
            for(let s1= start ; s1 < end ; s1 ++){
                sum +=extended[s1]
            }
              
        }   
        else{
            const base = index + n 
            const start = base + k  
            const end = base 
             for(let s1= start ; s1 < end ; s1 ++){
                sum +=extended[s1]
            }
        }
        return  sum 

    });
};
var numberOfAlternatingGroups = function(colors) {
    const arr = [... colors, colors[0],colors[1]]
    let sum = 0
    for( let i = 0 ; i < arr.length -2; i++){
        if (arr[i] === arr[i+2] && arr[i] !== arr[i+1] ){
            sum++
        }
    }
    return sum
};
var closestTarget = function(words, target, startIndex) {
    if (!words.some(x => x === target)){
        return -1
    }

    const indices = []
    words.forEach((value, index) => {
        if(words[index] === target){
            indices.push(index)
        }
    });
    const n = words.length
    let minDist = n;
    for(let i=0; i < indices.length ; i ++){
            const idx = indices[i];
            const d = Math.abs(startIndex - idx)
            const dist = Math.min(d,n-d) // one way and circular 
            minDist = Math.min(dist,minDist)
    }
    return minDist
};
var getDescentPeriods = function(prices) {
/*  let start=0
  let end =0 
  const longestSubArrays = []
  
  while( end < prices.length ){
    if( prices[end] - 1 === prices[end+1]){
        end +=1
    }
    else {
        longestSubArrays.push(prices.slice(start , end+1))
        end +=1
        start = end
    }
  }  
  function subArrays( arr) {
    const subArray = []
    for( let i =0 ; i <arr.length ; i++){
        for(let j=i ; j < arr.length ; j++){
            subArray.push(arr.slice(i,j+1))
        }
    }
    return subArray
  }
  const ans = []
  while(longestSubArrays.length !== 0){
        ans.push(subArrays(longestSubArrays.pop()))

  }
  return ans.flat().length */
    if (prices.length === 0) return 0;
    let ans = 0;
    let streak = 0; 
    for (let i = 0; i < prices.length; i++) {
        if (i > 0 && prices[i - 1] - 1 === prices[i]) {
        streak += 1;
        } else {
        streak = 1;
        }
        ans += streak; // all subarrays ending at i
    }

  return ans;
};
console.log(getDescentPeriods([3,2,1,4]))