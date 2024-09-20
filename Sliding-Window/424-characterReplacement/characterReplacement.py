class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        count = {}
        max_length = 0

        left_pointer = 0

        for right_pointer in range(len(s)):

            count[ s[right_pointer] ] = count.get(s[right_pointer], 0) + 1

            while((right_pointer - left_pointer + 1) - max(count.values())) > k :

                count[ s[left_pointer] ] -= 1
                left_pointer += 1

            max_length = max(max_length, (right_pointer - left_pointer + 1))

        
        return max_length





