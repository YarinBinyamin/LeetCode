from typing import List
from typing import Optional
import math

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
                    while cur != None and cur.val == duplic:
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
    
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num  
        return result      
                    
    def numDecodings(self, s: str) -> int:    
        if len(s) == 0 or s[0] == '0':
            return 0
        dp = [0] * (len(s) + 1)
        dp[0] = 1  # empty string
        dp[1] = 1  # first char is valid (already checked)
        for i in range(2, len(s) + 1):
            one_digit = s[i-1]
            two_digits = s[i-2:i]
            if "1" <= one_digit <= "9":
                dp[i] += dp[i-1]
            if "10" <= two_digits <= "26":
                dp[i] += dp[i-2]
        return dp[len(s)]
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head
        dummy = ListNode(-1, head)
        before = dummy
        cur = head
        for _ in range(left - 1):
            before = before.next
            cur = cur.next
        n = right - left
        while n > 0:
            temp = cur.next
            cur.next = temp.next
            temp.next = before.next
            before.next = temp
            n -= 1
        return dummy.next
    def list_to_linked_list(lst: List[int]) -> Optional[ListNode]:
        if not lst:
            return None
        head = ListNode(lst[0])
        current = head
        for value in lst[1:]:
            current.next = ListNode(value)
            current = current.next
        return head
    
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        def rec(s: str, x: int, cur: str):
            if x == 0 and len(s) == 0:
                ans.append(cur[:-1])
                return
            if x == 0 or len(s) == 0:
                return
            rec(s[1:], x - 1, cur + s[:1] + '.')
            if len(s) >= 2 and s[0] != '0':
                rec(s[2:], x - 1, cur + s[:2] + '.')
            if len(s) >= 3 and s[0] != '0' and int(s[:3]) <= 255:
                rec(s[3:], x - 1, cur + s[:3] + '.')
        rec(s, 4, "")
        return ans 
    
    
    # Definition for a binary tree node.
    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right 
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return []
        def buildTrees(start, end):
            if start > end:
                return [None] 
            all_trees = []
            for i in range(start, end + 1):
                left_trees = buildTrees(start, i - 1)
                right_trees = buildTrees(i + 1, end)
                for left in left_trees:
                    for right in right_trees:
                        root = TreeNode(i)
                        root.left = left
                        root.right = right
                        all_trees.append(root)
            return all_trees
        return buildTrees(1, n)
    def numTrees(self, n: int) -> int:
        if  n == 0:
            return 0 

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:   
            def isMirror(left, right):
               if( left is None and right is None):
                return True
               else:
                   if left is None or right is None:   
                        return False
                   elif (left.val == right.val):
                       return isMirror(left.left, right.right) and isMirror(left.right, right.left)
                   else:
                       return False
            return isMirror(root.left,root.right)
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:  
        if root is None:
            return 
        acc: List[List[int]] = []
        def levelacc(node: Optional[TreeNode], i):
                if node is None:
                    return 
                if i >= len(acc):
                    acc.append([])
                acc[i].append(node.val)
                levelacc(node.left, acc, i+1)
                levelacc(node.right, acc, i+1)
                return acc
        levelacc(root, 0)
        return acc
    
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return [] 
        acc: List[List[int]] = []
        def levelacc(node: Optional[TreeNode], i , left : bool):
                if node is None:
                    return 
                if i >= len(acc):
                    acc.append([])
                if left:
                    acc[i].append(node.val)
                else:
                    acc[i].appendleft(node.val)
                if(left):
                    levelacc(node.left,  i+1, not left)
                    levelacc(node.right,  i+1,not left)
                else:
                    levelacc(node.right,  i+1,not left)
                    levelacc(node.left,  i+1, not left)
                return acc
        levelacc(root, 0, True)
        return acc  
    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        return 1 +max(self.maxDepth(root.right),self.maxDepth(root.left) )
    
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        return root
    
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None                   
        root = TreeNode(postorder[ -1])
        mid = inorder.index(postorder[-1])  
        root.left = self.buildTree( inorder[0: mid], postorder[ :len(postorder) - mid -1 ] )
        root.right = self.buildTree( inorder[mid + 1:], postorder[ len(postorder) - mid : mid] )
        return root
    
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        acc : List[List[int]] = []
        def Rec(node: Optional[TreeNode], i: int):
            if node is None:
                return
            if i >= len(acc):
                acc.append([])
            acc[i].append(node.val)
            Rec(node.left, i+1)
            Rec(node.right, i +1)

        Rec(root, 0)
        return acc[::-1]
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:  
        if nums is None or len(nums) == 0:
            return None
        mid = (len(nums) //2 )
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[0:mid])
        root.right = self.sortedArrayToBST(nums[mid +1 : len(nums)])
        return root
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:          
        if head is None: 
            return None
        if head.next is None:
            return TreeNode(head.val)
        slow = head
        fast = head
        mid =  slow
        
        while (fast is not None ) and fast.next is not None:
            mid=slow
            fast = fast.next.next
            slow= slow.next
        root = TreeNode(slow.val)
        mid.next= None
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(slow.next)
        return root
        
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def Rec(node):
            if node is None:
                return 0
            heightL=Rec(node.left)
            if heightL == -1 :
                return -1
            heightR=Rec(node.right)
            if heightR == -1 :
                return -1
            if abs(heightL - heightR) > 1:
                return -1
            return 1 + max(heightR,heightL)
        return Rec(root) != -1
    
    def maxDifference(self, s: str) -> int:  
        #counts = Counter(s)
        counts = {}
        for char in s:
            counts[char] = counts.get(char,0) + 1 # gets the current count or 0 if not exist - and add it 1
        filterEven = list(filter(lambda x: x % 2 == 0 , counts.values() ))
        filterOdd =  list(filter(lambda x: x % 2 == 1, counts.values() ))   
        maxOdd = max(filterOdd) if filterOdd else 0
        minEven = min(filterEven)   if filterEven else 0 
        return maxOdd - minEven
       
    def maximumLengthSubstring(self, s: str) -> int:       
        counts = {}
        maxLength = 0
        left = 0
        for right in range(len(s)):
            counts[s[right]] = counts.get(s[right],0) +1
            while(counts[s[right]] > 2):
                counts[s[left]] -=1
                left +=1
            curr = right - left +1
            maxLength = max(maxLength, curr)
        return maxLength
    
    def sumOfUnique(self, nums: List[int]) -> int:     
        counts = {}
        sum = 0
        for x in nums:
            c = counts.get(x,0) +1
            counts[x] = c
            if c == 1:
                sum +=x
            elif c == 2: 
                sum -=x
        return sum
    
    def stoneGameII(self, piles: List[int]) -> int:
        dp= {}
        def dfs(alice, i , M):
            if i == len(piles):
                return 0
            if (alice, i , M) in dp:
                return dp[(alice, i , M)]
            res = 0 if alice else float('inf')
            total = 0
            for x in range(1, 2 * M + 1):
                if i + x > len(piles):
                    break
                total += piles[i + x - 1]
                if alice:
                    res = max(res, total + dfs(False, i + x, max(M, x)))
                else:
                    res = min(res, dfs(True, i + x, max(M, x)))
            dp[(alice, i , M)] = res
            return res
        return dfs(True, 0, 1)  
        
    def countTriples(self, n: int) -> int:   
        counter = 0
        for a in range(1,n+1):
            for b in range(1,n+1):           
                c = a*a + b*b
                c = math.sqrt(c)
                if (c.is_integer() and  c<=n):
                    counter +=1
        return counter
    
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:  
        max_len = 0 #   generally max
        def rec(node): 
            nonlocal max_len  
            if node is None:
                return 0
            left_length =rec(node.left) 
            right_length = rec(node.right)
            
            left_ext = 0
            right_ext = 0
            if node.left and node.left.val == node.val:
                left_ext = left_length + 1

            if node.right and node.right.val == node.val:
                right_ext = right_length + 1
            
            max_len= max(max_len, left_ext+right_ext) # saving V shape if we have
            return max(left_ext,right_ext) # return the longest straight path for next compution 
        rec(root)
        return max_len
    def countOdds(self, low: int, high: int) -> int:
        sum = high - low +1 
        if sum % 2 == 0:
            return sum//2
        else :
            if low % 2 == 1 :
                return (sum //2) +1
        return sum //2 
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:  
        if head is None or head.next is None:
            return None
        if head.next.next is None:
            head.next = None
            return head  
        ans = head
        prev = head
        slow = head
        fast = head
        while fast.next is not None:
            prev= slow
            slow = slow.next
            fast = fast.next
            if fast.next is not None:
                fast = fast.next
        #replace
        prev.next = slow.next
        return ans     
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_array = s.split(" ")
        if len(pattern) != len(s_array):
            return False

        map_char_to_word = {}
        map_word_to_char = {}
        for char,word in zip(pattern,s_array):
            if char in map_char_to_word: # i have the char but it refferd for a different word
                if map_char_to_word[char] != word:
                    return False
            else: # we dont have the char in the map
                map_char_to_word[char] = word
            if word in map_word_to_char:
                if map_word_to_char[word] !=char :
                    return False
            else:
                map_word_to_char[word] = char
        return True
    def numSpecial(self, mat: List[List[int]]) -> int:
        count = 0
        row = {}
        columns ={}
        for i in range (len(mat)):
            for j in range (len(mat[i])):
                if mat[i][j] == 1:
                    row[i] = row.get(i,0) +1
                    columns[j] = columns.get(j,0) +1
        for i in range (len(mat)):
            for j in range (len(mat[i])):
                if mat[i][j] == 1:
                    if row[i] == 1 and columns[j] ==1  :
                        count +=1
        return count
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        arr = [0] * (n+1)
        arr[1] = 1
        whoCanShare= 0 # who can share a secret

        final = 0
        mod = 10**9 + 7
        for i in range(2,n+1):

            if i >= 1+ delay:
                whoCanShare = (whoCanShare + arr[i-delay]) % mod

            if i >= 1+ forget:
                whoCanShare = (whoCanShare- arr[i-forget] ) % mod 

            arr[i]=whoCanShare % mod
        for days in range (max(1,n-forget+1), n+1):
            final = (final + arr[days])%mod
        return final % mod
    def longestOnes(self, nums: List[int], k: int) -> int:
        """""
        cur_k =k
        if len(nums) == 1:
            if k>=0:
                return 1
            else:
                return 0
        start = 0 
        end = 0
        curr=0
        max_length= 0
        while end < len(nums):
            while end < len(nums) and start<=end and nums[end] == 1  :
                end +=1
                curr = end -start 
                max_length = max(max_length,curr)
                
            if end < len(nums) and nums[end] == 0 :
                if cur_k>0 and cur_k<=k:
                    cur_k-=1
                    end +=1
                    curr = end - start
                    max_length = max(max_length,curr)
                   
                else :
                    while end < len(nums) and start <= end and nums[start] ==1:
                        start +=1
                    if end < len(nums) and nums[start] ==0 and cur_k < k :
                        cur_k +=1
                        start +=1
                        curr = end - start 
                        max_length = max(max_length,curr)
        return max_length
    """""

        if len(nums) == 1:
            if k>=0:
                return 1
            else:
                return 0
        zeros_at_window= 0
        start = 0 
        end = 0
        curr=0
        max_length= 0
        while end < len(nums) and start <=end:
            if nums[end] ==0 :
                zeros_at_window +=1
            end +=1
            if zeros_at_window > k:
                if nums[start] ==0:
                    zeros_at_window -=1
                start +=1
            curr = end - start
            max_length= max(max_length, curr)
        return max_length
        
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        ans = 0
        i=0
        j=0
        while i < len(g) and j< len(s) :
                if s[i] >=g[j]:
                    ans+=1
                    i+=1
                    j+=1   
                else:
                    j+=1   
        return ans
    
    def lengthOfLastWord(self, s: str) -> int:
        arr = s.split(" ")
        for i in reversed(arr):
            if arr[i]>0:
                return len(arr[i]) 
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:    
        new = purchaseAmount % 10
        last = 0
        if new <=5 :
              last = purchaseAmount -new
        else :
            last = purchaseAmount + (10 -new) 
        return 100 - last  
    def getSmallestString(self, s: str) -> str:
        char_array = list(s)
        flag = False
        for i in range(len(char_array) -1) :
            if flag:
                break
            first =int(char_array[i])
            second = int(char_array[i +1])
            if (int(char_array[i]) > int(char_array[i +1])):
                if first ==0:
                    continue
                if second == 0 and first%2==0 : 
                    temp = char_array[i]
                    char_array[i]= char_array[i+1]
                    char_array[i+1] = temp
                    flag = True
                elif ((first % int(second) == 0) or ((second) % int(first) == 0)) :
                    temp = char_array[i]
                    char_array[i]= char_array[i+1]
                    char_array[i+1] = temp
                    flag = True


        return char_array.join("")
            
        
if __name__ == "__main__":
            sol = Solution()
            root = TreeNode(3)
            root.left = TreeNode(9)
            root.right = TreeNode(20)
            root.right.left = TreeNode(15)
            root.right.right = TreeNode(7)
            nums =[1,1,1,0,0,0,1,1,1,1,0]
            g =[1,2]
            s = [1,2,3]
            result = sol.findContentChildren(g,s)
            print("Result:", result)