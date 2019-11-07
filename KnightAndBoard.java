
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.Comparator;

public class KnightAndBoard{
    public int n;
    public boolean judge;
    public int[][] board;
    public KnightAndBoard(int n){
        this.n = n;
        this.judge = true;
        board = new int[n][n];
    }
    public static class Point{
        int x,y;
        public Point(int x, int y){
            this.x = x;
            this.y = y;
        }
        public int getX(){
            return this.x;
        }
        public int getY(){
            return this.y;
        }
    }
    public boolean travelBoard(Point start, int cnt){
        for(int[] row : board){
                        for(int num : row){
                            System.out.print(num + "\t");
                        }
                        System.out.println();
                    }
        this.board[start.x][start.y] = cnt;
        if(cnt == n*n){
            return true;
        }
        List<Point> ps =  possiblePoints(start,board);
        hardPoint(ps, board);

        while(!ps.isEmpty()){
            Point p = ps.remove(0);
            if(checkNext(board, p)){
                if(travelBoard(p, cnt+1))
                    return true;
            }
        }
        board[start.x][start.y] = 0;
        return false;

        // Point currentPoint = start;
        // for(int[] dir : dirs){
        //     Point nextPoint = new Point(currentPoint.x + dir[0], currentPoint.y + dir[1]);
        //     if(checkNext(board, nextPoint)){
        //         if(travelBoard(nextPoint, cnt+1))
        //             return true;
        //     }
        // }
        // board[start.x][start.y] = 0;
        // return false;

    }
    // public int[][] travelBoard(Point start){
    //     int[][] board = new int[this.n][this.n];
    //     for(int i=0; i<this.n; i++){
    //         for(int j=0; j<this.n; j++){
    //             board[i][j] = 0;
    //         }
    //     }
    //     Stack<Point> stack = new Stack<Point>();
    //     int i = 1;
    //     board[start.x][start.y] = i;
    //     stack.push(start);
    //     Point currentPoint = start;

    //     while(true){
    //         for(int[] row : board){
    //             for(int num : row){
    //                 System.out.print(num + "\t");
    //             }
    //             System.out.println();
    //         }
    //         List<Point> possiblePoints = possiblePoints(currentPoint, board);
    //         if(possiblePoints.size() == 0){
    //             // 回溯
    //             if(!stack.empty()){
    //                 stack.pop();
    //             }
                
    //             if(!stack.empty()){
    //                board[currentPoint.x][currentPoint.y] = 0;
    //                i--;
    //                currentPoint = stack.peek();
    //                continue;
    //             }else{
    //                 this.judge = false;
    //                 break;
    //             }
    //         }
    //         else if(possiblePoints.size() == 1){
    //             currentPoint = possiblePoints.get(0);
    //             stack.push(currentPoint);
    //         }
    //         else{
    //             currentPoint = hardPoint(possiblePoints, board);
    //             stack.push(currentPoint);
    //         }
    //         board[currentPoint.x][currentPoint.y] = ++i;
    //         if(i == n*n){
    //             break;
    //         }

    //     }
    //     return board;
    // }

    public List<Point> possiblePoints(Point currentPoint, int[][] board){
        int [][] dirs ={
            {-2, 1},{-1, 2},
            {1, 2},{2,1},
            {2, -1},{1, -2},
            {-1, -2},{-2, -1}
        };
        List<Point> possibleList = new ArrayList<Point>();
        for(int[] dir : dirs){
            Point nextPoint = new Point(currentPoint.x + dir[0], currentPoint.y + dir[1]);
            if(checkNext(board, nextPoint)){
                possibleList.add(nextPoint);
            }
        }
        return possibleList;
    }

    public boolean checkNext(int[][] board, Point nextPoint){
        return nextPoint.x > -1 && nextPoint.x < this.n && nextPoint.y > -1 && nextPoint.y < this.n
        && board[nextPoint.x][nextPoint.y] == 0;

    }

    public void hardPoint(List<Point> points, int[][] board){

        points.sort(new Comparator<Point>(){
            public int compare(Point p1, Point p2){
                int cnt1=  possiblePoints(p1, board).size();
                int cnt2 = possiblePoints(p2, board).size();
                if(cnt1 < cnt2){
                    return -1;
                }else if(cnt1 == cnt2){
                    return 0;
                }else{
                    return 1;
                }
            }
        });
        // int minIndex = 0;
        // List<Point> minPoint = possiblePoints(points.get(0), board);
        // for(int i=1; i<points.size(); i++){
        //     List<Point> nextPoint = possiblePoints(points.get(i), board);  
        //     if(nextPoint.size() < minPoint.size()){
        //         minIndex = i;
        //         minPoint = nextPoint;
        //     }
        // }
        // return points.get(minIndex);
    }
    
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        scanner.close();
        long startTime = System.currentTimeMillis();
        KnightAndBoard knightAndBoard = new KnightAndBoard(n);
        Point start = new KnightAndBoard.Point(0, 0);
        boolean f = knightAndBoard.travelBoard(start, 1);
        long endTime = System.currentTimeMillis(); //获取结束时间 

        System.out.println("程序运行时间："+ (endTime - startTime) + "ms");
        if(f){
            for(int[] row : knightAndBoard.board){
                for(int num : row){
                    System.out.print(num + "\t");
                }
                System.out.println();
            }
            System.out.println("Yes");
        }else{
            System.out.println("No");
        }
    }
}