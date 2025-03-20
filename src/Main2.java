

import java.util.*;

import static java.util.Arrays.asList;
import static java.util.Arrays.sort;

public class Main2 {
    public static class ListNode {
        int val;
        ListNode next;
        ListNode() {}
        ListNode(int val) { this.val = val; }
        ListNode(int val, ListNode next) { this.val = val; this.next = next; }
    }

    public static void main(String[] args) {
        ListNode head = new ListNode(1);
        head.next = new ListNode(2);
        head.next.next = new ListNode(3);
        head.next.next.next = new ListNode(4);
        head.next.next.next.next = new ListNode(5);
        int k = 2;
        rotateRight(head, k);
        }


    //38. countAndSay
    public static String countAndSay(int n) {
        if (n == 1) return "1";
        if (n == 2) return "11";
        String curStr = "11";
        for (int i = 3; i <= n; i++) {
            StringBuilder ans = new StringBuilder();
            int index = 0;
            while (index < curStr.length()) {
                char curValue = curStr.charAt(index);
                int counter = 0;
                while (index < curStr.length() && curStr.charAt(index) == curValue) {
                    counter++;
                    index++;
                }
                ans.append(counter).append(curValue);
            }
            curStr = ans.toString();
        }
        return curStr;
    }

    // 39. combinationSum
    public static List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> ans = new ArrayList<>();
        List<Integer> curComb = new ArrayList<>();
        recursive(candidates, target, 0, curComb, ans);
        return ans;
    }

    private static void recursive(int[] candidates, int target, int startIndex, List<Integer> curComb, List<List<Integer>> ans) {
        if (target == 0) {

            ans.add(new ArrayList<>(curComb));
            return;
        }
        for (int i = startIndex; i < candidates.length; i++) {
            if (candidates[i] > target) continue;
            curComb.add(candidates[i]);
            recursive(candidates, target - candidates[i], i, curComb, ans);
            curComb.remove(curComb.size() - 1);
        }
    }


    //40. Combination sum II
    public static List<List<Integer>> combinationSum2(int[] candidates, int target) {
        List<List<Integer>> ans = new ArrayList<>();
        List<Integer> curComb = new ArrayList<>();
        Arrays.sort(candidates);
        recursive2(candidates, target, 0, curComb, ans);
        return ans;
    }

    /// /// Microsoft task 1
    public int solution(int[] V, int[] A, int[] B) {
        ArrayList<ArrayList<Integer>> Graph = new ArrayList<>();
        for (int i = 0; i < V.length; i++) {
            Graph.add(new ArrayList<>()); // Add an empty list for each project
        }
        for (int i = 0; i < A.length; i++) {
            if (!Graph.get(A[i]).contains(B[i])) { // Check if the edge already exists
                Graph.get(A[i]).add(B[i]); // Add B[i] as a dependency of A[i]
            }
        }

        return 0;
    }

    private static void recursive2(int[] candidates, int target, int startIndex, List<Integer> curComb, List<List<Integer>> ans) {
        if (target == 0) {
            if (!ans.contains(curComb)) {
                ans.add(new ArrayList<>(curComb));
            }
            return;
        }
        for (int i = startIndex; i < candidates.length; i++) {
            if (i > startIndex && candidates[i] == candidates[i - 1]) continue;
            if (candidates[i] > target) break;
            curComb.add(candidates[i]);
            recursive2(candidates, target - candidates[i], i + 1, curComb, ans);
            curComb.remove(curComb.size() - 1);

        }
    }

    //43. Multipy Strings
    public static String multiply(String num1, String num2) {
        /// none efficient
//        int ans = 0 ;
//        int power = 1 ;
//        int nexPower = 1;
//        for(int i = num1.length() -1 ; i >=0 ; i --){
//            int cur1 = num1.charAt(i) - '0';
//            for(int j = num2.length() -1 ; j>=0 ; j-- ){
//                int cur2 = num2.charAt(j) - '0';
//                ans = ans + (cur1 * cur2 * power);
//                power = power * 10;
//            }
//        nexPower = nexPower* 10;
//        power = nexPower;
//        }
//    String str = ""+ ans;
//        return str;

        ///////////////

//        int[] arr = new int [num1.length() + num2.length()];
//        for(int i = num1.length()-1 ; i>=0 ; i-- ){
//            int c = num1.charAt(i) - '0';
//            int k = num2.length() -1 - i;
//            for (int j = num2.length() -1 ; j>=0 ; j--){
//                int curr = num2.charAt(j) - '0';
//                int sum = arr[k] + c*curr;
//                arr[k] = sum % 10;
//                arr[k+1] = sum /10;
//                k++;
//            }
//        }
//        int ans = 0;
//        int power =1;
//        for(int l=0; l < arr.length ; l++){
//            ans = ans + arr[l] * power;
//            power = power *10;
//
//        }
//        return "" + ans;


        /// ///////////////////

        if (num1.equals("0") || num2.equals("0")) return "0";

        int[] arr = new int[num1.length() + num2.length()];

        // Multiply each digit of num1 with each digit of num2
        for (int i = num1.length() - 1; i >= 0; i--) {
            int digit1 = num1.charAt(i) - '0';
            for (int j = num2.length() - 1; j >= 0; j--) {
                int digit2 = num2.charAt(j) - '0';
                int sum = digit1 * digit2 + arr[i + j + 1]; // Add previous carry
                arr[i + j + 1] = sum % 10; // Current digit
                arr[i + j] += sum / 10;    // Carry to the next digit
            }
        }

        // Convert the array to a string
        StringBuilder result = new StringBuilder();
        for (int num : arr) {
            if (!(result.length() == 0 && num == 0)) { // Skip leading zeros
                result.append(num);
            }
        }

        return result.toString();
    }

    // 45. jump
    public static int jump(int[] nums) {
        int jumps = 0;
        int currentEnd = 0;
        int farthest = 0;
        for (int i = 0; i < nums.length - 1; i++) {
            farthest = Math.max(farthest, i + nums[i]);
            if (i == currentEnd) {
                jumps++;
                currentEnd = farthest;
                if (currentEnd >= nums.length - 1) {
                    break;
                }
            }
        }

        return jumps;
    }

    // 46. Permutation
    public static List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> ans = new ArrayList<List<Integer>>();
        List<Integer> cur = new ArrayList<Integer>();
        permute(nums, ans, cur, 0);
        return ans;
    }

    public static void permute(int[] nums, List<List<Integer>> ans, List<Integer> cur, int index) {
        if (index == nums.length) {
            if (!ans.contains(cur))
                ans.add(cur);
        } else {
            for (int i = 0; i < nums.length; i++) {
                if (!cur.contains(nums[i])) {
                    cur.add(nums[i]);
                    permute(nums, ans, new ArrayList<>(cur), index + 1);
                    cur.remove(cur.size() - 1);
                }
            }
        }
    }

    // 47. Permutation II
    public static List<List<Integer>> permuteUnique(int[] nums) {
        List<List<Integer>> ans = new ArrayList<List<Integer>>();
        List<Integer> cur = new ArrayList<Integer>();
        boolean[] used = new boolean[nums.length];
        for (int i = 0; i < nums.length; i++) {
            used[i] = false;
        }
        permuteUnique(nums, ans, cur, 0, used);
        return ans;
    }

    public static void permuteUnique(int[] nums, List<List<Integer>> ans, List<Integer> cur, int index, boolean[] used) {
        if (index == nums.length) {
            if (!ans.contains(cur))
                ans.add(cur);
        } else {
            for (int i = 0; i < nums.length; i++) {
                if (i > 0 && nums[i] == nums[i - 1] && !used[i - 1]) {
                    continue;
                }
                if (!used[i]) {
                    cur.add(nums[i]);
                    used[i] = true;
                    permuteUnique(nums, ans, new ArrayList<>(cur), index + 1, used);
                    used[i] = false;
                    cur.remove(cur.size() - 1);

                }

            }
        }
    }

    //48. Rotate Image
    public static void rotate(int[][] matrix) {

//        for (int j = 0; j < matrix.length -1 ; j++) {
//            for (int i = j; i< matrix.length ; i++) {
//                    int temp = matrix[j][i];
//                    matrix[j][i] = matrix[(matrix.length -1 ) - j][i];
//                matrix[(matrix.length -1 ) - j][i] = temp;
//                }
//            }
        for (int j = 0; j <= (matrix.length - 1)  ; j++) {
            for (int i = j; i <= (matrix.length - 1) ; i++) {
                int temp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = temp;
            }
        }
        for (int i = 0; i < matrix.length   ; i++) {
            for (int j = 0; j < matrix.length / 2 ; j++) {
                int temp = matrix[i][j];
                matrix[i][j] = matrix[i][matrix.length -1 - j];
                matrix[i][matrix.length -1 - j]= temp;
            }
            }

    }
    // 49.group anagrams
    public static List<List<String>> groupAnagrams(String[] strs) {
    List<List<String>> ans = new ArrayList<>();
    Hashtable<String, List<String>> Hash = new Hashtable<>();
    for (String str : strs){
        String strI = SortString(str);
        if(Hash.containsKey(strI)){
            Hash.get(strI).add(str);
        }
        else{
            Hash.put(strI, new ArrayList<>());
            Hash.get(strI).add(str);
        }
    }
        return new ArrayList<>(Hash.values());
    }




    public static String SortString(String input){
        char [] array = input.toCharArray();
        Arrays.sort(array);
        return new String(array);
    }
    // 50.pow
    public static double myPow(double x, int n) {
        long nLong = n;
        if (nLong < 0) {
            x = 1 / x;
            nLong = -nLong;
        }
        double result = 1;
        double currentEven = x;

        while (nLong > 0) {
            if (nLong % 2 == 1) { // odd
                result = result * currentEven;
            }
            currentEven = currentEven * currentEven;
            nLong = nLong / 2;
        }
        return result;
    }

    // 53.maximum SaubArray
    public static int maxSubArray(int[] nums) {
        int start =0;
        int end = 0;
        int curSum =0;
        int maxStart =0;
        int maxEnd = 0;
        int maxSum =Integer.MIN_VALUE;

        for(int i =0 ; i < nums.length  ; i ++){
            curSum = curSum + nums[i];
            if (curSum > maxSum) {
                maxSum = curSum;
                maxStart = start;
                maxEnd = i;
            }
            if (curSum < 0) {
                curSum = 0;
                start = i + 1; // Move start to next index
            }
        }

        return maxSum;

    }

    // 54. Spiral Matrix
   public static List<Integer> spiralOrder(int[][] matrix) {
       List<Integer> ans = new ArrayList<>();
       if (matrix == null || matrix.length == 0) return ans;

       int top = 0, bottom = matrix.length - 1;
       int left = 0, right = matrix[0].length - 1;

       while (top <= bottom && left <= right) {
           for (int i = left; i <= right; i++) {
               ans.add(matrix[top][i]);
           }
           top++;

           for (int i = top; i <= bottom; i++) {
               ans.add(matrix[i][right]);
           }
           right--;

           if (top <= bottom) {
               for (int i = right; i >= left; i--) {
                   ans.add(matrix[bottom][i]);
               }
               bottom--;
           }

           if (left <= right) {
               for (int i = bottom; i >= top; i--) {
                   ans.add(matrix[i][left]);
               }
               left++;
           }
       }

       return ans;
   }
   //1567. Maximum Length of subarray with positive product
   public static int getMaxLen(int[] nums) {
        if(nums.length == 1 && nums[0]>0){
            return 1;
        }
        if(nums.length == 2){
            if((nums[0] >0 && nums[1] > 0) || (nums[0] <0 && nums[1] < 0)) return 2;
            if(nums[0] >0 || nums[1]>0) return 1;
        }
        int product =1 ;
        int start = 0 ;
        int end = 0 ;
        int maxLength = 0 ;
        int curlength = 0;
        for(int i = 0 ; i < nums.length ; i ++) {
            if (nums[i] == 0) {
                if (curlength > maxLength) {
                    if (product > 0) {
                        maxLength = curlength;

                    } else if (curlength - 1 > maxLength) {
                        if ((product / nums[start]) > 0 || (product / nums[end-1]) > 0) {
                            maxLength = curlength - 1;
                        }
                    }

                }
                curlength = 0;
                start = i + 1;
                end = i + 1;
                product = 1;
            } else {
                product = product * nums[i];
                end++;
                curlength++;
                if (product > 0 && curlength > maxLength) {
                    maxLength = curlength;
                }

            }
        }
        return maxLength;
   }

   // 55. JumpGame
   public static boolean canJump(int[] nums) {
        if(nums.length == 0 )
            return false;
        if ( (nums.length == 1) && nums[0] == 0 )
            return true;
        int index = 0;
        int end = nums.length;
       int next = index;
        while(index <= end){
            int maxJump = index + nums[index] ;
            for(int i = index ; i <= index + nums[index] ; i++) {
                if (maxJump <= i + nums[i]) {
                    next = i;
                    maxJump = i + nums[i];
                }
                if (maxJump >= nums.length - 1) {
                    return true;
                }
            }
                index = next;
                if(nums[index] == 0 ){
                    return false;
                }


        }
       return false;
   }
    public static int[][] merge(int[][] intervals) {
//          if (intervals == null || intervals.length == 0) return null;
//        int [] [] result = new int[intervals.length][2];
//        ArrayList<int[]> list = new ArrayList<>();
//        int idx = 0;
//            for(int i = 0 ; i < intervals.length  - 1; i ++){
//                if(intervals[i][1] >= intervals[i+1][0]){
//                    int[] temp = {intervals[i][0], intervals[i+1][1]};
//                    list.add(temp);
//
//                    result[idx][0] = intervals[i][0];
//                    result[idx][1] = intervals[i+1][1];
//                    i++;
//                }
//                else{
//                    int[] temp = {intervals[i][0], intervals[i][1]};
//                    list.add(temp);
//
//                    result[idx][0] = intervals[i][0];
//                    result[idx][1] = intervals[i][1];
//                }
//                idx++;
//            }
//            if(result[idx][1] < intervals[intervals.length - 1][0]){
//                int[] temp = {intervals[intervals.length - 1][0], intervals[intervals.length - 1][1]};
//                list.add(temp);
//                result[idx][0] = intervals[intervals.length - 1][0];
//                result[idx][1] = intervals[intervals.length - 1][1];
//            }
//
//           return list.toArray(new int[list.size()][]);
        List<int[]> result = new ArrayList<>();
        int [] current = intervals[0];
        for (int i = 1; i < intervals.length; i++) {
            if(current[1] >= intervals[i][0]){
                current[1] = Math.max(current[1], intervals[i][1]);
            }
            else {
                result.add(current);
                current = intervals[i];
            }
        }
        result.add(current);

        return result.toArray(new int[result.size()][]);

    }

    public static int[][] insert(int[][] intervals, int[] newInterval) {
            int [][] newIntervals = Arrays.copyOf(intervals, intervals.length + 1);
            newIntervals[intervals.length] = newInterval;
            Arrays.sort(newIntervals, (a,b) -> Integer.compare(a[0],b[0]));
            int [] current = newIntervals [0];
            List<int[]> ans = new ArrayList<>();
            for (int i = 1; i < newIntervals.length; i++) {
                if(current[1] >= newIntervals [i][0]){
                    current[1] = Math.max(current[1], newIntervals[i][1]);
                }
                else{
                    ans.add(current);
                    current = newIntervals[i];
                }
            }
            ans.add(current);
            return ans.toArray(new int[ans.size()][]);

    }

    public static int[][] generateMatrix(int n) {
        int [][] result = new int[n][n];
        ArrayList<Integer> temp = new ArrayList<>();
        for(int i = 1 ; i <= n*n ; i++) {
            temp.add(i);
        }
        temp.sort(Integer::compare);
        int left = 0 ,up = 0 ;
        int right = n-1, bottom = n-1;
        while(left <= right & up <= bottom){
            for(int i = left ; i <= right ; i++){
                result[up][i] = temp.removeFirst();
            }
            up++;
            for(int i = up ; i <= bottom ; i++){
                result[i][right] = temp.removeFirst();
            }
            right--;
            for(int i = right ; i >= left ; i--){
                result[bottom][i] = temp.removeFirst();
            }
            bottom--;
            for(int i = bottom ; i >= up ; i--){
                result[i][left] = temp.removeFirst();
            }
            left++;
        }
        return result;

    }


    public static ListNode rotateRight(ListNode head, int k) {
        if (k == 0 || head == null) {
            return head;
        }
        int size = 1;
        ListNode temp = head;

        while ( temp.next != null){
            temp = temp.next;
            size++;
        }
        k %= size;
        if(k == 0) {
            return head;
        }
        temp.next = head;
        int steps = size - k;
        ListNode newTail = head;
        for (int i = 1; i < steps; i++) {
            newTail = newTail.next;
        }
        ListNode newHead = newTail.next;
        newTail.next = null;

        return newHead;

    }

}



