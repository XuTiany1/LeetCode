class Solution:


    def productExceptSelf(self, nums: List[int]) -> List[int]:

        num_length = len(nums)
        results = [1] * num_length

        curr_prefix_product = 1
        curr_suffix_product = 1

        for i in range(num_length):
            results[i] = curr_prefix_product
            curr_prefix_product *= nums[i]

        # Start index - Stop index - Step
        for i in range(num_length-1, -1, -1):
            results[i] *= curr_suffix_product
            curr_suffix_product *= nums[i]

        return results