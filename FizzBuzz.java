import java.util.Scanner;

public class FizzBuzz {

    public static void Fizz_Buzz(int number) {
        for (int i = 1; i <= number; i++) {
            if (i % 3 == 0 & i % 5 == 0) {
                System.out.println(i + " FizzBuzz");
            }
            else if (i % 3 == 0) {
                System.out.println(i + " Fizz");
            }
            else if (i % 5 == 0) {
                System.out.println(i + " Buzz");
            }
            else {
                System.out.println(i);
            }
        }
    }

    public static void main(String[] args) {
        System.out.print("Please enter the number: ");
        Scanner numberScan = new Scanner(System.in);
        int number = numberScan.nextInt();
        Fizz_Buzz(number);
        numberScan.close();
    }
}
