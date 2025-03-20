import org.w3c.dom.Node;
import org.w3c.dom.NodeList;

import java.util.*;
import java.util.LinkedList;

// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) {
        int arr1[] = {1, 3, 5, 6};
        int arr2[] = {1, 3};
        //i want to test 3 sum
//        int arr3[] = {-1, 0, 1, 2, -1, -4};
//        List<List<Integer>> result = threeSum(arr3);
//        for (int i = 0; i < result.size(); i++) {
//            System.out.println(result.get(i));
//        }
//    List<String> ans = generateParenthesis(3);
//   for( int i = 0; i < ans.size() ; i++){
//       System.out.println(ans.get(i));
//   }
        //      System.out.println(divide(10, 5));
//
        System.out.println(searchInsert(arr2, 2));

    }

    //Merge and Sort
    public static int[] mergeSort(int[] arr) {
        if (arr == null) {
            throw new RuntimeException("empty arr");
        }
        if (arr.length < 2) {
            return arr;
        }
        int[] arr1 = splitLeft(arr);
        int[] arr2 = splitRight(arr);

        arr1 = mergeSort(arr1);
        arr2 = mergeSort(arr2);

        return merge(arr1, arr2);
    }

    public static int[] splitLeft(int[] arr) {
        int[] output = new int[arr.length / 2];
        for (int i = 0; i < arr.length / 2; i++) {
            output[i] = arr[i];
        }
        return output;
    }

    public static int[] splitRight(int[] arr) {
        int[] output = new int[arr.length - arr.length / 2];
        for (int i = arr.length / 2; i < arr.length; i++) {
            output[i - arr.length / 2] = arr[i];
        }
        return output;
    }


    public static int[] merge(int[] arr1, int[] arr2) {
        int index = 0;
        int i1 = 0;
        int i2 = 0;
        int[] output = new int[arr1.length + arr2.length];
        while (i1 < arr1.length & i2 < arr2.length & index < output.length) {
            if (arr1[i1] < arr2[i2]) {
                output[index] = arr1[i1];
                i1++;
            } else {
                output[index] = arr2[i2];
                i2++;
            }
            index++;

        }
        while (i1 < arr1.length) {
            output[index] = arr1[i1];
            i1++;
            index++;
        }
        while (i2 < arr2.length) {
            output[index] = arr2[i2];
            i2++;
            index++;
        }
        return output;
    }

    /// // Randomized Select - Return the i's smallest element in array (n)
    public static int randomizedSelect(int[] A, int l, int r, int i) {
        if (l == r) {
            return A[i];
        }
        int p = RandomizedPartition(A, l, r); // return pivot index
        int k = p - l + 1; // all the elemnts that smaller than pivot
        if (k == i) {  // k = the number of elemnts that smaller than pivot, the index is plus 1 ("p = k +1 ") the index of the smallest
            return A[p];
        } else if (i < k) {
            return randomizedSelect(A, l, p, i);
        } else {
            return randomizedSelect(A, p + 1, r, i - k);
        }


    }

    public static int select(int[] A, int l, int r, int i) {
        if (l == r) {
            return A[i];
        }
        int j = choosePivot(A, l, r); // choose the pivot
        int temp = A[j];
        A[j] = A[r];
        A[r] = temp; // put the pivot at the end
        int p = partition(A, l, r); // partition the array by the pivot
        int k = p - l + 1; // all the elemnts that smaller than pivot
        if (k == i) {  // k = the number of elemnts that smaller than pivot, the index is plus 1 ("p = k +1 ") the index of the smallest
            return A[p];
        } else if (i < k) {
            return randomizedSelect(A, l, p, i);
        } else {
            return randomizedSelect(A, p + 1, r, i - k);
        }
    }


    public static int choosePivot(int[] A, int l, int r) {
        if (r - l < 5) {
            return partition(A, l, r);
        }
        int n = r - l + 1; // number of elements
        int m = (n + 4) / 5; // number of medians
        int[] medians = new int[m];
        for (int i = 0; i < m; i++) {
            int l1 = l + 5 * i;
            int r1 = Math.min(l1 + 4, r);
            medians[i] = choosePivot(A, l1, r1);
        }
        return choosePivot(medians, 0, m - 1);
    }

    /// // Partition in with Randomized pivot
    private static int RandomizedPartition(int[] a, int l, int r) {
        int i = (int) (Math.random() * (r - l) + l); // choosing a random location
        int temp = a[r];
        a[r] = a[i];
        a[i] = temp; //put the pivot at the end and doing partition
        return partition(a, l, r);

    }

    // QuickSort
    private static void QuickSort(int[] arr, int l, int r) { //Sort an array n^2 (best case n*logn)
        if (l < r) {
            int pi = partition(arr, l, r); // choosing pivot (put each element by < > )
            QuickSort(arr, l, pi - 1); // subArray
            QuickSort(arr, pi + 1, r); // subArray
        }
    }

    /// // Retrun the index of the pivot after the array sorted by smaller and bigger number of the pivot (n)
    private static int partition(int[] arr1, int low, int high) {
        int pivot = arr1[high]; // taking the highest index one
        int i = low - 1;
        for (int j = low; j < high; j++) {
            if (arr1[j] < pivot) { // each element which is smaller than
                i++;
                int temp = arr1[i];
                arr1[i] = arr1[j];
                arr1[j] = temp; //exchange places between the bound of i to the j's
            }
        }
        int temp = arr1[i + 1];
        arr1[i + 1] = arr1[high];
        arr1[high] = temp; // exchange the pivot
        return i + 1;
    }

    /// //Return the index of the element v in the array (log(n))
    private static int BinarySearch(int[] arr1, int v) {
        int start = 0;
        int end = arr1.length;
        while (start <= end) {
            int mid = (start + end) / 2;
            if (arr1[mid] == v) {
                return mid;
            } else if (arr1[mid] < v) {
                start = mid + 1;
            } else {
                end = mid - 1;
            }

        }
        return -1;
    }

    private static double findMedianSortedArrays(int[] arr1, int[] arr2) {
        if (arr1.length > arr2.length) {
            return findMedianSortedArrays(arr2, arr1);
        }

        int n = arr1.length;
        int m = arr2.length;
        int start = 0;
        int end = n;
        while (start <= end) {
            int partitionX = (start + end) / 2;
            int partitionY = (m + n + 1) / 2 - partitionX;

            int maxX = (partitionX == 0) ? Integer.MIN_VALUE : arr1[partitionX - 1];
            int minX = (partitionX == n) ? Integer.MAX_VALUE : arr1[partitionX];

            int maxY = (partitionY == 0) ? Integer.MIN_VALUE : arr2[partitionY - 1];
            int minY = (partitionY == m) ? Integer.MAX_VALUE : arr2[partitionY];

            if (maxX <= minY && maxY <= minX) {
                // found the correct partition
                if ((n + m) % 2 == 0) {
                    return ((double) Math.max(maxX, maxY) + Math.min(minX, minY)) / 2;
                } else {
                    return Math.max(maxX, maxY);
                }
            } else if (maxX > minY) {
                // move towards the left in nums1
                end = partitionX - 1;
            } else {
                start = partitionX + 1;
            }
        }
        throw new IllegalArgumentException();
    }

    private static void InsertionSort(int[] arr) {
        for (int h = 0; h < arr.length; h++) {
            System.out.print(arr[h] + " ");
        }
        for (int i = 1; i < arr.length; i++) {
            int temp = arr[i];
            int j = i - 1;
            while ((j >= 0) && (arr[j] > temp)) {
                arr[j + 1] = arr[j];
                j--;
            }
            arr[j + 1] = temp;
        }
        System.out.println();
        for (int h = 0; h < arr.length; h++) {
            System.out.print(arr[h] + " ");
        }

    }

    // 3. Length of longest substing
    public int lengthOfLongestSubstring(String s) {
        HashSet<Character> mySub = new HashSet<>(); // To store unique characters in the current window
        int maxSize = 0; // To store the length of the longest substring
        int left = 0;    // Left pointer of the sliding window

        // Iterate with the right pointer through the string
        for (int right = 0; right < s.length(); right++) {
            // If the current character is already in the set, shrink the window from the left
            while (mySub.contains(s.charAt(right))) {
                mySub.remove(s.charAt(left)); // Remove the leftmost character
                left++; // Move the left pointer to the right
            }
            // Add the current character to the set and update the max size
            mySub.add(s.charAt(right));
            maxSize = Math.max(maxSize, right - left + 1);
        }
        return maxSize;
    }

    // 5. LongestPalindrome
    public static String longestPalindrome(String s) {

        if (s == null || s.length() < 1) return "";
        int left = 0;
        int right = 0;
        for (int i = 0; i < s.length(); i++) {
            int sub1 = expandAroundCeneter(s, i, i); // odd length
            int sub2 = expandAroundCeneter(s, i, i + 1); // even length
            int maxlen = Math.max(sub1, sub2);
            if (maxlen > right - left) { // check if the new Palindrom is longer than the pervious
                left = i - ((maxlen - 1) / 2);
                right = i + (maxlen / 2); // palindrome is symmetric so add half

            }
        }
        return s.substring(left, right + 1);


    }


    public static int expandAroundCeneter(String s, int left, int right) {
        while ((left >= 0) && (right < s.length()) && (s.charAt(left) == s.charAt(right))) {
            right++;
            left--;
        }
        return right - left - 1;
    }

    // 6. ZigZag - my solution which have problems when the string is long
    public static String convert(String s, int numRows) {
        if (numRows == 1) {
            return s;
        }
        int group = numRows + (numRows - 2); // size of group
        int numOfFullgroups = s.length() / group; // how many groups
        int res = (s.length() % group) * group; // the res
        int numCol = 0;
        if (res <= numRows) {
            numCol = numOfFullgroups + numOfFullgroups * (numRows - 2) + 1;
        } else {
            numCol = numOfFullgroups + numOfFullgroups * (numRows - 2) + 1 + (res - numRows);
        }

        char[][] arr = new char[numCol][numRows];
        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr[0].length; j++) {
                arr[i][j] = '0';
            }
        }

        int j = 0;
        while (s.length() != 0) {
            int h = 0;
            for (int i = 0; (s.length() != 0) && (i < numRows); i++) {
                arr[j][i] = s.charAt(0);
                s = s.substring(1);
                h = i;
            }
            h = h - 1;
            j++;
            while ((s.length() != 0) && (h > 0)) {
                arr[j][h] = s.charAt(0);
                s = s.substring(1);
                h--;
                j++;
            }

        }
//        int group = numRows + (numRows - 2);
//        int numOfFullgroups = s.length() / group;
//        int res = (s.length() % group) * group;
//        int numCol = 0;
//        if (res <= numRows) {
//            numCol = numOfFullgroups + 1;
//        } else {
//            numCol = 1 + (res - numRows) + numOfFullgroups;
//        }
//
//        char[][] arr = new char[numCol][numRows];
//        for(int i = 0; i < arr.length; i++){
//            for(int j = 0; j < arr[0].length; j++){
//                arr[i][j] = '0';
//            }
//        }
//        for (int i = 0; i < arr.length && (s.length() != 0); i = i+ (numRows - 2)) {
//            for (int j = 0; j < numRows && (s.length() != 0) ; j++) {
//                arr[i][j] = s.charAt(0);
//                s = s.substring(1);
//            }
//            for (int i1 = numRows - 2; i1 >= 1 && (s.length() != 0); i1--) {
//
//                arr[i1][i1 + (i / res)] = s.charAt(0);
//                s = s.substring(1);
//
//            }
//
//        }
        String ans = "";
        for (int b = 0; b < arr[0].length; b++) {
            for (int a = 0; a < arr.length; a++) {
                if (arr[a][b] != '0') {
                    ans = ans + arr[a][b];
                }
            }
        }
        return ans;
    }

    public static String convert2(String s, int numRows) {
        // Edge case: If there's only one row, return the string as is
        if (numRows == 1) {
            return s;
        }

        // Create a list of StringBuilder, one for each row
        StringBuilder[] rows = new StringBuilder[Math.min(numRows, s.length())];
        for (int i = 0; i < rows.length; i++) {
            rows[i] = new StringBuilder();
        }
        int curRow = 0;
        boolean goingDown = false;

        // Traverse the string and place characters into the appropriate row
        for (char c : s.toCharArray()) {
            rows[curRow].append(c);

            // Change direction when we hit the top or bottom row
            if (curRow == 0 || curRow == numRows - 1) {
                goingDown = !goingDown;
            }

            // Move to the next row, either down or up
            curRow += goingDown ? 1 : -1;
        }

        // Combine all rows to form the final result
        StringBuilder result = new StringBuilder();
        for (StringBuilder row : rows) {
            result.append(row);
        }

        return result.toString();
    }


    public static String convert3Leet(String s, int numRows) {
        if (numRows == 1) {
            return s;
        }
        char[] chars = new char[s.length()];
        int cycle = 2 * numRows - 2;
        int k = 0;

        for (int row = 0; row < numRows; row++) {
            for (int i = row; i < s.length(); i += cycle) {
                chars[k++] = s.charAt(i);
                if (row > 0 && row < numRows - 1 && i + cycle - 2 * row < s.length()) {
                    chars[k++] = s.charAt(i + cycle - 2 * row);
                }
            }
        }
        return new String(chars);
    }

    public static int reverse(int x) {
        // this solution doenst check if it is outof the max/ min value
//        boolean positive = false;
//        if(x >= 0 )
//            positive = true ;
//        else{
//            x = -1 * x;
//        }
//        String Xstart = "" + x;
//        char [] arrString = Xstart.toCharArray();
//        int j = 1;
//        int ans= 0 ;
//        for(int i = 0 ; i < arrString.length ; i++) {
//            int num = arrString[i] - '0';
//            ans = ans + (num * j);
//            j= j * 10;
//        }
//
//        if(!positive){
//            ans = -1 * ans;
//        }
//        return ans;
        ////////////////////////

        int rev = 0;
        while (x != 0) {
            int digit = x % 10;
            x = x / 10;

            if ((rev > Integer.MAX_VALUE / 10) || ((rev == Integer.MAX_VALUE / 10) && (digit > 7))) {
                return 0;
            }
            if ((rev < Integer.MIN_VALUE / 10) || ((rev == Integer.MIN_VALUE / 10) && (digit < -8))) {
                return 0;
            }
            rev = rev * 10 + digit;

        }
        return rev;


    }

    // 9. isPalindrome
    public static boolean isPalindrome(int x) {
        if (x < 0) {
            return false;
        }
        boolean Pali = true;
        String newX = "" + x;
        int start = 0;
        int end = newX.length() - 1;
        while (Pali && newX.length() > 1) {
            if (newX.charAt(start) == newX.charAt(end)) {
                newX = newX.substring(1, newX.length() - 1);
                end = newX.length() - 1;
            } else {
                return false;
            }
        }
        return Pali;


    }

    public static int maxArea(int[] height) {
        int left = 0;
        int right = height.length - 1;
        int maxArea = 0;
        while (left < right) {
            int currentHeight = Math.min(height[right], height[left]);
            int currentWidth = right - left;
            int area = currentWidth * currentHeight;
            maxArea = Math.max(maxArea, area);

            if (height[right] < height[left]) {
                right--;
            } else {
                left++;
            }
        }
        return maxArea;
    }

    public static boolean isMatch(String s, String p) {
        // Base case: if both the string and the pattern are empty, it's a match
        if (p.isEmpty()) {
            return s.isEmpty();
        }

        // Check if the first character of the string matches the first character of the pattern
        boolean firstMatch = (!s.isEmpty() && (p.charAt(0) == s.charAt(0) || p.charAt(0) == '.'));

        // Handle the case when the next character in the pattern is '*'
        if (p.length() >= 2 && p.charAt(1) == '*') {
            // Option 1: Skip the current character and '*', which means zero occurrences of the preceding character
            // Option 2: Use the '*' to match at least one occurrence of the preceding character (if firstMatch is true)
            return (isMatch(s, p.substring(2)) || (firstMatch && isMatch(s.substring(1), p)));
        } else {
            // If there's no '*', continue to the next character in both the string and pattern
            return firstMatch && isMatch(s.substring(1), p.substring(1));
        }
    }

    // 12. IntegerToRoman
    public static String intToRoman(int num) {
        String ans = "";
        int[] numbers = {1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000};
        String[] strings = {"I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"};
        for (int i = numbers.length - 1; i >= 0; i--) {
            if (num - numbers[i] >= 0) {
                num = num - numbers[i];
                ans = ans + strings[i];
                i++;
            }
        }
        return ans;

    }

    // 13. RoamnToIntger
    public static int romanToInt(String s) {
        Map<Character, Integer> list = new HashMap<>();
        list.put('I', 1);
        list.put('V', 5);
        list.put('X', 10);
        list.put('L', 50);
        list.put('C', 100);
        list.put('D', 500);
        list.put('M', 1000);
        int result = list.get(s.charAt(s.length() - 1));
        for (int i = s.length() - 2; i >= 0; i--) {
            if (list.get(s.charAt(i)) < list.get(s.charAt(i + 1))) {
                result = result - list.get(s.charAt(i));
            } else {
                result = result + list.get(s.charAt(i));
            }

        }

        return result;
    }

    // 14.LongestPrefix
    public static String longestCommonPrefix(String[] strs) {
        if (strs == null || strs[0] == null) {
            return "";

        }
        for (int i = 0; i < strs[0].length(); i++) {
            char c = strs[0].charAt(i);
            for (int j = 1; j < strs.length; j++) {
                if (i >= strs[j].length() || strs[j].charAt(i) != c) {
                    return strs[0].substring(0, i);
                }
            }
        }
        return strs[0];
    }

    // 15. 3sum
    public static List<List<Integer>> threeSum(int[] nums) {
        if (nums.length < 3) {
            return new ArrayList<>();
        }
        ArrayList<List<Integer>> output = new ArrayList<>();
        Arrays.sort(nums);
        for (int i = 0; i < nums.length - 2; i++) {
            if (i > 0 && nums[i] == nums[i - 1]) {
                continue;
            }
            int left = i + 1;
            int right = nums.length - 1;
            while (left < right) {
                int sum = nums[i] + nums[left] + nums[right];
                if (sum == 0) {
                    output.add(Arrays.asList(nums[i], nums[left], nums[right]));
                    while (left < right && nums[left] == nums[left + 1]) {
                        left++;
                    }
                    while (left < right && nums[right] == nums[right - 1]) {
                        right--;
                    }
                    right--;
                    left++;

                } else if (sum < 0) {
                    left++;
                } else {
                    right--;
                }

            }

        }
        return output;
    }

    // 16. 3sumClosest
    public static int threeSumClosest(int[] nums, int target) {
        Arrays.sort(nums);
        int closest = nums[0] + nums[1] + nums[2];
        for (int i = 0; i < nums.length - 2; i++) {
            int left = i + 1;
            int right = nums.length - 1;
            while (left < right) {
                int sum = nums[i] + nums[left] + nums[right];
                if (Math.abs(target - sum) < Math.abs(target - closest)) {
                    closest = sum;
                }
                if (target - sum > 0) {
                    left++;
                } else {
                    right--;
                }
            }
        }
        return closest;
    }

    // 17. lettersCombination
    public static List<String> letterCombinations(String digits) {
        char[][] letters = {{}, {}, {'a', 'b', 'c'}, {'d', 'e', 'f'}, {'g', 'h', 'i'}, {'j', 'k', 'l'}, {'m', 'n', 'o'}, {'p', 'q', 'r', 's'}, {'t', 'u', 'v'}, {'w', 'x', 'y', 'z'}};
        ArrayList<String> ans = new ArrayList<>();
        letterCombinations(0, "", digits, ans, letters);
        return ans;
    }

    public static void letterCombinations(int i, String curStr, String digits, ArrayList<String> ans, char[][] letters) {
        if (curStr.length() == digits.length()) {
            ans.add(curStr);
            return;
        }
        if (i < digits.length()) {
            char spec = digits.charAt(i);
            char[] arr = letters[spec - '0'];

            for (char c : arr) {
                letterCombinations(i + 1, curStr + c, digits, ans, letters);
            }
        }
    }

    // 18. FourSum
    public static List<List<Integer>> fourSum(int[] nums, int target) {
        ArrayList<List<Integer>> ans = new ArrayList<List<Integer>>();
        Arrays.sort(nums);
        if (nums.length < 4) {
            return ans;
        }
        for (int mainLeft = 0; mainLeft < nums.length - 2; mainLeft++) {
            for (int mainRight = nums.length - 1; 2 < mainRight; mainRight--) {
                int newRight = mainRight - 1;
                int newLeft = mainLeft + 1;
                while (newLeft < newRight) {
                    double sum = (double) nums[mainLeft] + (double) nums[newLeft] + (double) nums[newRight] + (double) nums[mainRight];
                    if (sum == target) {
                        List<Integer> find = Arrays.asList(nums[mainLeft], nums[newLeft], nums[newRight], nums[mainRight]);
                        if (!ans.contains(find))
                            ans.add(find);
                    }
                    if (sum > target) {
                        newRight--;
                    } else {
                        newLeft++;
                    }
                }

            }
        }
        return ans;
    }


    // 20. isValid
    public static boolean isValid(String s) {
        Stack<Character> elemnts = new Stack<>();
        if (s.length() == 1) return false;

        for (int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);
            if (ch == '[' || ch == '{' || ch == '(') {
                elemnts.push(ch);
            } else if (elemnts.isEmpty()) {
                return false;
            } else {
                char c = elemnts.pop();
                if ((c == '[' && s.charAt(i) != ']') || (c == '{' && s.charAt(i) != '}') || (c == '(' && s.charAt(i) != ')'))
                    return false;
            }
        }
        return elemnts.isEmpty();
    }


    // 22. Generate Parentheses
    public static List<String> generateParenthesis(int n) {
        ArrayList<String> ans = new ArrayList<String>();
        String curStr = "";
        generateParenthesis(ans, curStr, n, n);
        return ans;


    }

    public static void generateParenthesis(List<String> ans, String curStr, int open, int close) {
        if ((open < 0) || (close < 0) || open > close)
            return;
        if (open == 0 && close == 0) {
            ans.add(curStr);
            return;
        }
        if (close >= 0 || open >= 0) {
            generateParenthesis(ans, curStr + '(', open - 1, close);
            generateParenthesis(ans, curStr + ')', open, close - 1);
        }


    }

    // 26. Remove Duplicates from Sorted Array
    public static int removeDuplicates(int[] nums) {
        int left = 0;
        int right = nums.length;
        int i = 1;
        while (i < nums.length) {
            if (!(nums[left] < nums[i])) {
                i++;
            } else {
                nums[left + 1] = nums[i];
                i++;
                left++;
            }
        }
        return left + 1;
    }

    // 27. Remove elements
    public static int removeElement(int[] nums, int val) {
        if (nums.length == 1) {
            if (nums[0] == val) {
                nums = new int[0];
                return 0;
            } else return nums.length;
        }
        int left = 0;
        int right = nums.length - 1;
        while (left <= right) {
            if (nums[left] != val) {
                left++;
            } else {
                nums[left] = nums[right];

                right--;
            }
        }
        int[] arr1 = new int[left];
        for (int i = 0; i < left; i++) {
            arr1[i] = nums[i];
        }
        nums = arr1;
        return nums.length;
    }

    // 28. Find the Index of the First Occurrence in a String
    public static int strStr(String haystack, String needle) {
        if (haystack.length() < needle.length())
            return -1;
        int start = 0;
        for (int i = 0; i < haystack.length(); i++) {
            if (needle.charAt(0) == haystack.charAt(i)) {
                start = i;
                for (int j = 0; j < needle.length() && (i + j) < haystack.length(); j++) {
                    if (needle.charAt(j) != haystack.charAt(i + j)) {
                        break;
                    }
                    if (j == needle.length() - 1) {
                        return start;
                    }
                }
            }
        }
        return -1;
    }

    // 29. Divide Two Integers
    public static int divide(int dividend, int divisor) {
        if (divisor == 0) throw new ArithmeticException("Dividing by zero");
        if ((dividend == Integer.MAX_VALUE) && divisor == -1) return Integer.MIN_VALUE;
        if ((dividend == Integer.MIN_VALUE) && divisor == -1) return Integer.MAX_VALUE;
        if ((dividend == Integer.MAX_VALUE) && divisor == 1) return Integer.MAX_VALUE;
        if ((dividend == Integer.MIN_VALUE) && divisor == 1) return Integer.MIN_VALUE;

        boolean negative = (dividend < 0) ^ (divisor < 0); // XOR operation, if both same - returns false
        long absDividend = Math.abs((dividend));
        long absDivisor = Math.abs((divisor));
        int quotinet = 0;

        while (absDividend >= absDivisor) {
            long tempDivisor = absDivisor;
            int multiple = 1;

            while ((tempDivisor << 1) <= absDividend) {
                tempDivisor <<= 1;
                multiple <<= 1;
            }
            absDividend -= tempDivisor;
            quotinet += multiple;
        }
        return negative ? -quotinet : quotinet;
    }

    // 30. Find substring concatetion of  all words
    public static List<Integer> findSubstring(String s, String[] words) {
        List<Integer> result = new ArrayList<>();
        int lengthOfPermutaion = words.length * words[0].length();
        HashMap<String, Integer> wordCount = new HashMap<>();
        int wordLength = words[0].length();
        for (String word : words) {
            wordCount.put(word, wordCount.getOrDefault(word, 0) + 1);
        }
        for (int i = 0; i <= s.length() - lengthOfPermutaion; i++) {

            HashMap<String, Integer> windowSlideMap = new HashMap<>();
            int j = 0;
            while (j < words.length) {
                int wordStart = i + j * wordLength;
                String curStr = s.substring(wordStart, wordStart + wordLength);
                if (wordCount.containsKey(curStr)) {
                    windowSlideMap.put(curStr, windowSlideMap.getOrDefault(curStr, 0) + 1);

                    if (windowSlideMap.get(curStr) > wordCount.get(curStr)) {
                        break;
                    }
                } else {
                    break;
                }
                j = j + wordLength;

            }
            if (j == words.length) {
                result.add(i);
            }


        }
        return result;
    }

    public static void subInsertionsort(int[] arr, int pivot) {
        for (int i = pivot; i < arr.length; i++) {
            int temp = arr[i];
            int j = i - 1;
            while ((j >= pivot) && (arr[j] > temp)) {
                arr[j + 1] = arr[j];
                j--;
            }
            arr[j + 1] = temp;
        }

    }

    // 31. Next Permutation
    public static void nextPermutation(int[] nums) {
        int pivot = -1;
        ;
        for (int i = nums.length - 2; i >= 0; i--) {
            if (nums[i] < nums[i + 1]) {
                pivot = i;
                break;
            }
        }
        if (pivot == -1) {
            int start = 0;
            int end = nums.length - 1;
            while (start < end) {
                int change = nums[start];
                nums[start] = nums[end];
                nums[end] = change;
                start++;
                end--;
            }
            return;
        }
        for (int i = nums.length - 1; i > pivot; i--) {
            if (nums[i] > nums[pivot]) {
                int temp = nums[i];
                nums[i] = nums[pivot];
                nums[pivot] = temp;
                break;
            }
        }
        subInsertionsort(nums, pivot + 1);
    }


    //33.
    public static int search(int[] nums, int target) {
        int left = 0;
        int right = nums.length - 1;
        boolean find = false;
        while (!find) {
            int mid = (left + right) / 2;
            if (target == nums[mid]) {
                return mid;
            }
            if (target == nums[left]) {
                return left;
            }
            if (target == nums[right]) {
                return right;
            }
            if (right == left || left == mid || right == mid) {
                return -1;
            }
//            else if (target <= nums[mid] && (nums[left] <= target)) {
//                right = mid -1 ;
//            } else {
//                left = mid + 1 ;
//            }
            if (nums[left] < nums[mid]) {
                if (target <= nums[mid] && (nums[left] <= target)) {
                    right = mid - 1;
                } else {
                    left = mid + 1;
                }
            } else if (nums[mid] < nums[right]) {
                if ((nums[mid] <= target && target <= nums[right])) {
                    left = mid + 1;
                } else {
                    right = mid - 1;
                }

            }


        }
        return -1;
    }

    // 34. Find first and last position of element in sorted array
    public static int[] searchRange(int[] nums, int target) {
        int[] ans = {-1, -1};
        int left = 0;
        int right = nums.length - 1;
        while (left <= right) {
            int mid = (left + right) / 2;
            if (nums[mid] == target) {
                if (ans[0] == -1 || mid < ans[0]) {
                    ans[0] = mid;
                }
                if (ans[1] == -1 || mid > ans[1]) {
                    ans[1] = mid;
                }
                if (nums[left] == target) {
                    ans[0] = Math.min(ans[0], left);
                }
                if (nums[right] == target) {
                    ans[1] = Math.max(ans[1], right);
                }

                left++;
                right--;
            } else if (nums[mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        return ans;
    }

    // 35. Search Insert Position
    public static int searchInsert(int[] nums, int target) {
        int left = 0;
        int right = nums.length - 1;
        while (left <= right) {
            int mid = (left + right) / 2;
            if (nums[mid] == target) {
                return mid;
            }
            // left not found
            else if (target < nums[mid]) {
                if (mid == 0) {
                    return 0;
                } else if (nums[mid - 1] < target) {
                    return mid;
                } else {
                    right = mid - 1;
                }
            }
            // right not found
            else if (nums[mid] < target) {
                if (mid == nums.length - 1) {
                    return nums.length;
                } else if (target < nums[mid + 1]) {
                    return mid + 1;
                } else {
                    left = mid + 1;
                }
            }

        }
        return -1;
    }


    public static boolean isValidSudoku(char[][] board) {
        HashSet<String> seen = new HashSet<>();

        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                char num = board[i][j];
                if (num != '.') {
                    if (!seen.add(num + " in row " + i) ||
                            !seen.add(num + " in col " + j) ||
                            !seen.add(num + " in box " + (i / 3) + "-" + (j / 3))) {
                        return false; // If duplicate found, return false
                    }
                }
            }
        }
        return true; // If no duplicate found, return true
    }

}
    // 100. SameTree
//    public static boolean isSameTree(TreeNode p, TreeNode q) {
//        if( q == null && p == null) return true;
//        if( q == null || p == null || (q.val != p.val)) return false;
//        return isSameTree(p.left,q.left) && isSameTree(q.right,p.right);
//
//    }












