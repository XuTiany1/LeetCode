class Solution:

    """
    def majorityElement(self, nums: list[int]) -> int:

        threshold = (len(nums)/2)

        count_dictionary = {}

        for current_value in nums:

            if current_value in count_dictionary:
                
                count_dictionary[current_value] += 1
            
            else:

                count_dictionary[current_value] = 1

            if count_dictionary[current_value] >= threshold:
                return current_value

        return -1
    """

    def majorityElement(self, nums: list[int]) -> int:

        candidate = -1
        count = 0

        for current_number in nums:

            if count == 0:
                candidate = current_number
                count += 1

            elif (candidate != current_number):
                count -= 1
            
            else:
                count += 1

        return candidate


nums = [2,2,1,1,1,2,2]
nums2 = [3,2,3]
solution = Solution()
majority = solution.majorityElement(nums2)

print(majority)