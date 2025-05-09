class Solution:
    def expand_around_center(self, s: str, left: int, right: int) -> str:
        """
        expand_around_center

        Function to determine a palindrome based expanding the range of left and right
        around the center of the string.

        :param s: The string to be expanded
        :param left: The left index of the string
        :param right: The right index of the string
        :return: The valid palindrome after overshooting
        """
        while left >= 0 and right < len(s) and s[left] == s[right]: # Whole left and right are within the string and the same
            left -= 1
            right += 1

        # Reaching this point means either the left or right of the string is out of bounds or are different characters
        # If either left or right is out of bounds, the whole string is a palindrome, so return the whole string
        # If we reach this point because the left and right are different characters, only the valid portion which is a palindrome is returned

        return s[left + 1:right]  # The valid palindrome after overshooting

    def longestPalindrome(self, s: str) -> str:
        # Initialize the longest palindrome to an empty string
        longest = ""
        for i in range(len(s)): # for each index within the string
            # Odd length
            p1 = self.expandAroundCenter(s, i, i)
            # Even length
            p2 = self.expandAroundCenter(s, i, i + 1)

            # Update the longest palindrome
            if len(p1) > len(longest): # We have found a longer palindrome
                longest = p1
            if len(p2) > len(longest): # We have found a longer palindrome
                longest = p2

        return longest

