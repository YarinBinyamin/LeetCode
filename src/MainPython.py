from typing import List


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
        directories = path.split("/")
        stack = []
        for dir in directories:
            if dir == "" or dir == ".": #if it's empty skip this componet
                continue
            elif dir == "..": # we need to go one directory back
                if stack:  
                    stack.pop()
            else: # add it
                stack.append(dir)
        return "/" + "/".join(stack) #between components / and then at the end
    
    def minDistance(self, word1: str, word2: str) -> int:
        arr = [[float("inf")]*(len(word2) +1) for i in range(len(word1) + 1)] #2 dimensional array
        
        for j in range (len(word2) + 1):
            arr[len(word1)][j] = len(word2) -j
        for i in range (len(word1) +1):
            arr[i][len(word2)] = len(word1) - i
        
        for i in range (len(word1) -1,-1,-1):
            for j in range (len(word2) -1,-1,-1):
                if word1[i] == word2[j]:
                    arr[i][j] = arr[i+1][j+1]
                else:
                    arr[i][j] = 1+ min(arr[i+1][j],arr[i+1][j+1],arr[i][j+1])
        return arr[0][0]
    
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        i=0
        j=0
        changed = False
        while i < len(matrix):
            while j < len(matrix[0]):
                if matrix[i][j] == 0:
                    setThezero(matrix, i , j)
                    i=i+1
                    j=j+1
                else:
                    j=j+1
                    changed = True
            if changed:
                i=i+1
                j=0
                changed = False
                           
        
        
    def setTheZero(matrix: List[List[int]], col : int, row :int ) -> None:
        for i in range (len(matrix)): #clear col
            matrix[i][col] = 0
        for j in range (len(matrix[0])):
            matrix[row][j] = 0
        
        
if __name__ == "__main__":
    sol = Solution()
    arr = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    result = sol.setZeroes(arr)
    print("Result:", result)