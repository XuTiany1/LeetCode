class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        

        curr_char_index_dict = {}
        curr_start = 0
        max_length = 0


        for end, char in enumerate(s):

            if (char in curr_char_index_dict) and (curr_char_index_dict[char] >= curr_start):

                curr_start = curr_char_index_dict[char] + 1
            
            curr_char_index_dict[char] = end

            max_length = max(max_length, end - curr_start + 1)


        return max_length

