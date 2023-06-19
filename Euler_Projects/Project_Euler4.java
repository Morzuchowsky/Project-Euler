public class Project_Euler4 {
    public static void main(String[] args) {
        //A palindromic number reads the same both ways.
        //The largest palindrome made from the product of two-digit numbers is 9009 == 91 X 99
        //Find the largest palindrome made from the product of two 3-digit numbers.

        int largestPalindrome = 0;
        for (int i = 999; i > 99; i--) {
            for (int l = 999; l > 99; l--) {
                int palindromeNumber = i * l;
                String intToString = String.valueOf(palindromeNumber);
                char[] stringToCharArray = intToString.toCharArray();

                boolean isPalindrome = true;


                for (int k = 0; k < stringToCharArray.length / 2; k++) {
                    char firstChar = stringToCharArray[k];
                    char lastChar = stringToCharArray[stringToCharArray.length - k - 1];
                    if (firstChar != lastChar) {
                        isPalindrome = false;
                        break;
                    }
                }
                if (isPalindrome && palindromeNumber > largestPalindrome) {
                    largestPalindrome = palindromeNumber;
                }
            }
        }
        System.out.println("This is Palindrome number: " + largestPalindrome);
    }
}



