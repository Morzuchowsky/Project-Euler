public class Project_Euler6 {
    //1^2 + 2^2 + ... + 10^2 = 385.
    //The square of the sum of the first ten natural numbers is,
    //(1 + 2 + ... + 10)^2 = 55^2 = 3025.
    //Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.
    //Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
    public static void main(String[] args) {
        int sumOfTheSquares = 0;
        int squareOfTheSum = 0;
        for (int i = 1; i <= 100; i++) {
            sumOfTheSquares = sumOfTheSquares + (i * i);
        }
        for (int k = 1; k <= 100; k++) {
            squareOfTheSum = k + squareOfTheSum;
        }
        System.out.println(squareOfTheSum * squareOfTheSum - sumOfTheSquares);
    }
}
