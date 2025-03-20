class Solution(object):
    def lengthOfLastWord(self, s):
        char = ' '
        length = 0
        for i in range(len(s) -1, -1 ,-1):
            if s[i] != char:
                length += 1           
            elif length > 0:
                return length     
        return length
        """
        :type s: str
        :rtype: int
        """
    def addBinary(self, a, b):
        i,j = len(a) -1, len(b) -1
        carry = 0
        result = []
        while i >= 0 or j >=0:
            digit_a = int(a[i]) if i>=0 else 0
            digit_b = int(b[j]) if j>=0 else 0
            sum = carry + digit_a + digit_b
            carry = sum // 2
            result.append(sum % 2)
            i-=1
            j-=1
        if carry:
            result.append(carry)
        return ''.join(map(str, result[::-1]))    
        """
        :type a: str
        :type b: str
        :rtype: str
        """
    def permute(self, nums):
    ans_list = []  # This will store the final permutations
    mid_list = []  # Temporary list to store the current permutation
    self.recper(ans_list, mid_list, 0, nums)
    return ans_list

    def recper(self, ans_list, mid_list, index, nums):
        if index == len(nums):
            if mid_list not in ans_list:  # Avoid duplicate permutations
                ans_list.append(list(mid_list))  # Append a copy of mid_list
            return
        
        for i in range(len(nums)):
            if nums[i] not in mid_list:  # Check if the element is already in mid_list
                mid_list.append(nums[i])  # Add element to the current permutation
                self.recper(ans_list, mid_list, index + 1, nums)  # Recur with updated list
                mid_list.pop()  # Backtrack by removing the last added element          
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
    def generateMatrix(self, n):
        num = 1
        left = 0
        up = 0
        right = n-1
        bottom = n-1
        ans = [[0] * n for _ in range(n)]
        while left <= right and up <= bottom:
            for i in range(left, right +1 ):
                ans[up][i] = num
                num +=1 
            up += 1
            for i in range(up, bottom  +1):
                ans[i][right] = num
                num += 1
            right -= 1
            if up <= bottom:
                for i in range(right, left - 1, -1):
                    ans[bottom][i] = num
                    num += 1
                bottom -= 1 
            if left <= right:
                for i in range(bottom, up - 1, -1):
                    ans[i][left] = num
                    num += 1
                left += 1  
        return ans

if __name__ == "__main__":
    sol = Solution()
    example_string = "Hello World   "
    result = sol.lengthOfLastWord(example_string)
    print(f"Length of last word: {result}")        
    binary1 = "1010"
    binary2 = "1011"
    binary_result = sol.addBinary(binary1, binary2)
    print(f"Binary addition result: {binary_result}")  # Expected: "10101"