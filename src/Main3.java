import javax.management.openmbean.CompositeType;
import java.util.ArrayList;
import java.util.Arrays;

public class Main3 {

    public static void main(String[] args) {
        int [][] obstacleGrid1 = {{0,0,0},{0,1,0},{0,0,0}};
        int [][] obstacleGrid2 = {{0,1},{0,0}};
        int [] sum = {8,9,9,9};
       int [] ans=  plusOne(sum);
        System.out.println(uniquePathsWithObstacles(obstacleGrid2));
    }
    //62
    public static int uniquePaths(int m, int n) {
        if (m == 1 || n == 1) return 1;
        int[][] grid = new int[m][n];
        grid[0][0] = 1;
        for(int i= 0; i <= m-1 ; i++){
            grid[i][0] = 1;
        }
        for(int j= 0; j <= n-1 ; j++){
            grid[0][j] = 1;
        }
        for(int i= 1; i <= m-1 ; i++){
            for(int j = 1 ; j <= n-1 ; j++){
                    grid[i][j] = grid[i -1 ][j] + grid[i][j - 1];

            }
        }
        return grid[m-1][n-1];

    }
    //63
    public static int uniquePathsWithObstacles(int[][] obstacleGrid) {
        int m = obstacleGrid.length;
        int n = obstacleGrid[0].length;
        if( (obstacleGrid[0][0] == 1) || (obstacleGrid[m-1][n-1] == 1)){
            return 0;
        }
        int [][] grid = new int[m][n];
        grid [0][0] = 1;
        int signI = 1;
        int signJ = 1;
        for(int i= 0; i <= m-1 ; i++){
            if (obstacleGrid[i][0] == 1) {
                signI = 0;
            }
            grid[i][0] = signI;
        }
        for(int j= 0; j <= n-1 ; j++){
            if (obstacleGrid[0][j] == 1) {
                signJ = 0;
            }
            grid[0][j] = signJ;
        }
        for(int i= 1; i <= m-1 ; i++){
            for(int j = 1 ; j <= n-1 ; j++){
                if (obstacleGrid[i][j] == 1 )   {
                    grid[i][j] =0;
                }
                else {
                    grid[i][j] = grid[i - 1][j] + grid[i][j - 1];
                }
            }
        }
        return grid[m-1][n-1];

    }
    //64
    public int minPathSum(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        int [][] minSumGrid = new int[m][n];
        minSumGrid[0][0] = grid[0][0];
        for(int i= 1; i <= m-1 ; i++){
            minSumGrid[i][0] = minSumGrid[i-1][0] + grid[i][0];
        }
        for(int j= 1; j <= n-1 ; j++) {
            minSumGrid[0][j] = minSumGrid[0][j-1] + grid[0][j];
        }

        for(int i= 1; i <= m-1 ; i++) {
            for (int j = 1; j <= n - 1; j++) {
            minSumGrid[i][j] = grid[i][j] + Math.min(minSumGrid[i-1][j],minSumGrid[i][j-1]);
            }
        }
        return minSumGrid[m-1][n-1];
    }

    //66
    public static int[] plusOne(int[] digits) {
        ArrayList<Integer> ans = new ArrayList<>();
        int carry = 1;
        for (int i = digits.length - 1; i >= 0; i--) {
            int curr = digits[i] + carry;
            ans.addFirst(curr % 10);
            carry = curr / 10;
        }
        if (carry > 0) {
            ans.addFirst( carry);
        }
        int[] ansArr = new int[ans.size()];
        for (int i = 0; i < ans.size(); i++) {
            ansArr[i] = ans.get(i);
        }

        return ansArr;
    }
}
