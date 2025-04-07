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
        First_Row_HasZero = False
        First_Col_HasZero = False
        for i in range(len(matrix)): #first Col
            if matrix[i][0] == 0:
                First_Col_HasZero = True
                break
        for j in range(len(matrix[0])): #first Row
            if matrix[0][j] == 0:
                First_Row_HasZero = True     
                break
        
        # if matrix[i][j] = 0 -> matrix[0][j] & matrix[i][0] = 0
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
                    
        for i in range(1, len(matrix)):
            if matrix[i][0] == 0:
                for j in range(1, len(matrix[0])):
                    matrix[i][j] = 0
                    
        for j in range(1, len(matrix[0])):
            if matrix[0][j] == 0:
                for i in range(1, len(matrix)):
                    matrix[i][j] = 0 
                    
        if  First_Row_HasZero:
            for j in range (len(matrix[0])):
                matrix[0][j] = 0
                
        if First_Col_HasZero:
            for i in range (len(matrix)):
                matrix[i][0] = 0
        return matrix
                 
            
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) - 1
        arr_index_search = -1
        while (left <= right):
            mid = ((left + right) // 2) 
            if matrix[mid][0] <= target and target <= matrix[mid][len(matrix[0]) - 1]:
                arr_index_search= mid 
                break
            elif  target <=  matrix[mid][0]:
                right = mid -1
            else:
                left = mid +1 
        if arr_index_search == -1:
            return False
        
        left = 0
        right = len(matrix[0]) - 1
        while left <= right:
            mid = (left + right) // 2 
            if matrix[arr_index_search][mid] == target:
                return True
            elif matrix[arr_index_search][mid] < target:
                left = mid +1
            else:
                right = mid -1
            return False
    
        def sortColors(self, nums: List[int]) -> None:
            count = [0] * 3  
            for num in nums:
                count[num] += 1 
            
            index = 0
            for i in range(3):  
                while count[i] > 0:  
                    nums[index] = i
                    index += 1
                    count[i] -= 1
                
            
            
        
                                       
        
        
  
        
if __name__ == "__main__":
    sol = Solution()
    arr = [2,2]
    result = sol.sortColors(arr)
    print("Result:", result)