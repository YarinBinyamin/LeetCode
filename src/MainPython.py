from typing import List
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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
                    
    def combine(self, n: int, k: int) -> List[List[int]]:
        array_of_arrays = []
        self.combineRec(n,k,array_of_arrays,[], 1)
        return array_of_arrays
        
    def combineRec(self, n: int , k: int, array_of_arrays: List[List[int]], array :List[int], start : int ):
        if k ==0 :
                array_of_arrays.append(array.copy())
                return
        else:
            for i in range (start, n+1 , +1):
                    array.append(i)
                    self.combineRec(n,k-1,array_of_arrays, array, i + 1)
                    array.pop()
                    
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        rec = []
        ans = []
        
        def subset(start):
            if ans is not None :rec.append(ans.copy())
            for i in range(start, len(nums)):
                ans.append(nums[i])
                subset(i + 1)
                ans.pop()
        subset(0)
        rec.remove(rec[0])
        
        return rec
    def exist(self, board: List[List[str]], word: str) -> bool:
        pairs_starts= []
        for i in range (len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    pairs_starts.append([i,j])
        for pair in pairs_starts:
            boolBoard = [[False] * len(board[0]) for _ in range(len(board))]
            boolBoard[pair[0]][pair[1]] = True
            if self.exist_one(board, word[1:], pair[0], pair[1], boolBoard):
                return True
        return False
            
    
    
    def exist_one(self, board: List[List[str]], word: str, i : int, j: int,  boardBool: List[List[bool]]) -> bool:
        if len(word) == 0:
            return True
        else :
            if i-1 >= 0 and board[i-1][j] == word[0] and  boardBool[i-1][j] == False:
                boardBool[i-1][j] = True
                if self.exist_one(board, word[1:], i-1, j, boardBool):
                    return True
                boardBool[i-1][j] = False            
            if i+1 <(len(board)) and board[i+1][j] == word[0] and  boardBool[i+1][j] == False:
                boardBool[i+1][j] = True
                if self.exist_one(board, word[1:], i+1, j, boardBool):
                    return True
                boardBool[i+1][j] = False
            if j-1 >= 0 and board[i][j-1] == word[0] and  boardBool[i][j-1] == False:
                boardBool[i][j-1] = True
                if self.exist_one(board, word[1:], i, j-1, boardBool):
                    return True
                boardBool[i][j-1] = False
            if j+1 <(len(board[0])) and board[i][j+1] == word[0] and  boardBool[i][j+1] == False:
                boardBool[i][j+1] = True
                if self.exist_one(board, word[1:], i, j+1, boardBool):
                    return True
                boardBool[i][j+1] = False
        return False
    
    def removeDuplicates(self, nums: List[int]) -> int:
        twice = False
        last = nums[0]
        for i in range (1,len(nums)):
            if nums[i] != last :
                last = nums[i]
                twice = False
            elif nums[i] == last and not twice:
                twice = True
            elif nums[i] == last and twice:
                nums[i] = pow(10,4) + 1
        list.sort(nums)
        k=0
        i=0
        while i < (len(nums)) and nums[i] <= pow(10,4):
            k = k +1 
            i = i+1
        return k   
     
    def search(self, nums: List[int], target: int) -> bool:
        left = 0
        right = len(nums) -1
        while left <= right:
            mid = left + (right - left) // 2 
            if nums[mid] == target:
                return True
            if nums[left] < nums[mid]: #left side
                if nums[left] <= target < nums[mid]: # inside left side
                    right = mid -1 
                else:
                    left = mid + 1        
            elif nums[left] > nums[mid]: # right side
                if nums[mid] < target <= nums[right]: # inside right side
                    left = mid + 1
                else:
                    right = mid -1
            else:
                left += 1 
        return False
    
    # Definition for singly-linked list.
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
            sentinal = ListNode(-1)
            sentinal.next = head
            prev = sentinal
            cur = head
            while cur != None:
                if cur.next != None and cur.val == cur.next.val:
                    duplic = cur.val
                    while cur != Nones and cur.val == duplic:
                        cur = cur.next
                    prev.next = cur
                else:
                    prev = cur
                    cur = cur.next
            return sentinal.next
    def deleteDuplicatesEasy(self, head: Optional[ListNode]) -> Optional[ListNode]:
            sentinal = ListNode(-1)
            sentinal.next = head
            prev = sentinal
            cur = head
            while cur != None:  
                if cur.next != None and cur.val == cur.next.val:
                    cur.next = cur.next.next
                    prev.next = cur
                else:   
                    prev = cur
                    cur = cur.next
            return sentinal.next
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
            sentinalL = ListNode(-1)
            curL = sentinalL
            sentinalR = ListNode(-1)
            curR = sentinalR
            curI = head
            
            while curI != None: 
                nextNode = curI.next
                curI.next = None
                
                if curI.val < x:
                    curL.next = curI
                    curL = curL.next
                else:
                    curR.next = curI
                    curR = curR.next
                curI = nextNode
            curL.next = sentinalR.next
            return sentinalL.next 
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        A = m-1
        B = n-1
        C = m+n-1
        while A >= 0 and B >= 0:
            if nums1[A] > nums2[B]:
                nums1[C] = nums1[A]
                A -= 1
            else:
                nums1[C] = nums2[B]
                B -= 1
            C -= 1
        while B >= 0:
            nums1[C] = nums2[B]
            B -= 1
            C -= 1
    def grayCode(self, n: int) -> List[int]:
        list = [0] *((2**n) )
        list [0] = 0
        if(n==0):
            return list
        list[1] = 1
        cur = 1
        index =2
        for i in range(2,n+1):
            cur *=2  # 01(1),10(2),100(4)
            for j in range(cur-1,-1,-1) :
                list[index]= cur + list[j]
                index +=1  
        return list     
 #   def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            ans = [[], [nums[0]]]
            return ans
        ans =[]
        ans.append([])
        for size in range(1,len(nums)):
            self.recSubSet(nums,size,ans,temp=[], index=0 )
        ans.append(nums)
        return ans
        
 #   def recSubSet(self, nums: List[int], size:int, ans : List[List[int]], temp: List[int], index:int):
        if len(temp) == size:
            if temp not in ans:
                ans.append(temp.copy())
                return
        for i in range(index,len(nums)):
            temp.append(nums[i])
            self.recSubSet(nums,size, ans, temp , index +1)
            temp.pop()
            self.recSubSet(nums,size, ans, temp,index +1)
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Sort first to group duplicates
        ans = []
        def recSubSet(start: int, path: List[int]):
            ans.append(path.copy())
            for i in range(start, len(nums)):
                if(i > start and nums[i] == nums[i-1]):
                    continue
                path.append(nums[i])
                recSubSet(i + 1, path)
                path.pop()
        recSubSet(0, [])
        return ans
    
    # Definition for a binary tree node.


    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        def recIn(curRoot: Optional[TreeNode]):
            if not curRoot:
                return
            recIn(curRoot.left)
            ans.append(curRoot.val)
            recIn(curRoot.right)

        recIn(root)
        return ans
    def maxProfit1(self, prices: List[int]) -> int:
        index_buy = 0
        max_profit = 0
        for i in range(len(prices)):
            if (prices[index_buy] > prices[i]):
                index_buy = i
            profit_today = prices[i] - prices[index_buy]
            if(max_profit < profit_today):
                max_profit = profit_today
        return max(max_profit,0)
                
                    
    
    
            
if __name__ == "__main__":
        sol = Solution()
        nums1 =[0,3,8,6,8,6,6,8,2,0,2,7]
        nums2 = [7,1,5,3,6,4]
        result = sol.maxProfit1(nums2)
        print("Result:", result)