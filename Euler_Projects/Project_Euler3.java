import java.util.Scanner;

public class Project_Euler3 {
    public static void main(String[] args) {
        //The prime factors of 13195 are 5, 7, 13 and 29.
        //What is the largest prime factor of the number 600851475143?
        long number = 600851475143L;
        for (int i = 2; i < number; i++) {
            while (number % i == 0) {
                System.out.println(i + " ");
                number = number / i;
            }
        }
        if (number > 2) {
            System.out.println(number);
        }
    }
}

