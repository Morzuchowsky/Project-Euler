public class Project_Euler5 {
    public static void main(String[] args) {
        //2520  is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
        //What is the smallest positive number that is evenly divisible by all the numbers from 1 to 20?

        int smallestMultiply = 20;
        int result = 1;
        while (smallestMultiply > 0) {
            if (result % smallestMultiply != 0) {
                result++;
                smallestMultiply = 20;
            } else if (result % smallestMultiply == 0) {
                smallestMultiply--;
            }
        }
        System.out.println(result);
    }
}

