class Solution:


    def isPalindrome(self, s: str) -> bool:

        s = s.lower()

        filter_str = ''

        for char in s:

            if char.isalnum():
                filter_str += char

        return (filter_str == filter_str[::-1])

        




