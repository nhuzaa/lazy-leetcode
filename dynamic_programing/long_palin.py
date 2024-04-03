"""
Given a string s, return the longest 
palindromic

https://leetcode.com/problems/longest-palindromic-substring/description/
 
substring in s.

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.


"""


class Solution(object):
    def longestPalindrome(self, s):
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        start, maxLength = 0, 1

        # all substring of lenght 1 is palindrom
        for i in range(n):
            dp[i][i] = True

        # all substring for lenght 2
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                start = i
                maxLength = 2

        # now check for more than
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                if s[i] == s[j] and dp[i + 1] == dp[j - 1]:
                    dp[i][j] = True
                    start = i
                    maxLength = length

        return s[start : start + maxLength]


input = "babad"
S = Solution()
output = S.longestPalindrome(input)
print(output)
