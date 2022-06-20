class Solution {
    public boolean isPalindrome(int x) {
		int intput = x;
        int temp, revert = 0;
        while (intput > 0) {
            revert *= 10;
            revert += intput%10;
            intput /= 10;
        }
        return revert == x;
    }
}