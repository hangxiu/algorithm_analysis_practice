import java.io.IOException;
import java.util.Scanner;

public class Long_Nonasc_Seq{
    private int N;
    private double[] in;
    private int[] tem_long;
    private int result;
    // private int[] next_pos;

    public Long_Nonasc_Seq(int n, double[] in_){
        this.tem_long = new int[n];
        this.in = new double[n];
        // this.next_pos = new int[n];
        this.N = n;
        this.result = 0;
        for(int i=0; i<this.N;i++){
            this.in[i] = in_[i];
        }

        
    }
    public int Cal_Long_Nonasc_Seq(){
       
        tem_long[N-1] = 1;
        // next_pos[N-1] = N-1;
        for(int i=this.N-2; i>=0; i--){
            // int Max = 0;
            //int nextPos = i;
            for(int j=i+1; j < this.N ;j++){
                if(in[j] < in[i]){
                    // if(tem_long[j] > Max){
                    //     Max = tem_long[j];
                    //     nextPos = j;
                    // }
                    tem_long[i] = Math.max(tem_long[i], tem_long[j] + 1); 
                }
            }
            // tem_long[i] = Max + 1;
            // next_pos[i] = nextPos;
            this.result = Math.max(result, tem_long[i]);
        } 

        return this.result;
    }
    // public void Print_Path(){
    //     int maxS=0;
    //     for(;maxS < N;maxS++){
    //         if(tem_long[maxS] == result){
    //             break;
    //         }
    //     }
    //     int nextPos = maxS;
    //     while(nextPos != next_pos[nextPos]){
    //         System.out.printf("%.1f ",in[nextPos]);
    //         nextPos = next_pos[nextPos];
    //     }

    //     System.out.printf("%.1f\n", in[nextPos]);

    //     for(int i=0;i<N-1;i++){
    //         System.out.printf("%d ",next_pos[i]);
    //     }
    //     System.out.printf("%d\n", next_pos[N-1]);
    // }
    void Print_Path_Im(){
        int me_t  = result;
            
        for(int i=0;i<N;i++){
            if(tem_long[i] == me_t){
                System.out.printf("%.1f ",in[i]);   
                me_t--;
            }
           
        }
        System.out.printf("\n");
    }  

    public Long_Nonasc_Seq(){
        
        this.result = 0; 
        System.out.println("请输入序列长度");
        Scanner scanner = new Scanner(System.in);
        this.N= scanner.nextInt();
        this.in = new double[N];
        this.tem_long = new int[N];
        // this.next_pos = new int[N];

        System.out.println("序列数");
        for(int i=0; i<this.N; i++){
            this.in[i] = scanner.nextDouble();
        }
    }

    public static void main(String[] args) {
        Long_Nonasc_Seq lns;
       
        int n =8;
        double[] in = {8, 6,5,10,9,	7,3,2};
        lns = new Long_Nonasc_Seq(n, in);
        // lns = new Long_Nonasc_Seq();
        int re = lns.Cal_Long_Nonasc_Seq();
        System.out.printf("result = %d\n", re);
        // lns.Print_Path();
        lns.Print_Path_Im();
        
    }

}