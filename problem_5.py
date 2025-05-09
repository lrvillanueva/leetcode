class Solution:
    def expandAroundCenter(self, s: str, left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]  # The valid palindrome after overshooting

    def longestPalindrome(self, s: str) -> str:
        longest = ""
        for i in range(len(s)):
            # Odd length
            p1 = self.expandAroundCenter(s, i, i)
            # Even length
            p2 = self.expandAroundCenter(s, i, i + 1)

            # Update the longest palindrome
            if len(p1) > len(longest):
                longest = p1
            if len(p2) > len(longest):
                longest = p2

        return longest

