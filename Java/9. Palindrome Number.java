class Solution {
    public boolean isPalindrome(int x) {
        if (x < 0) return false;
		int intput = x;
        int temp, revert = 0;
        while (intput >= 10) {
            revert *= 10;
            revert += intput%10;
            intput /= 10;
        }
        return revert == x/10 && intput == x%10;
    }
}