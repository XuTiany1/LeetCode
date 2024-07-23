class Solution:
    
    def remove_element(self, nums: list[int], val: int) -> int:

        good_value_list = []

        for i in range(len(nums)):
            if nums[i] != val:
                good_value_list.append(nums[i])

        for i in range(len(good_value_list)):
            nums[i] = good_value_list[i]

        return len(good_value_list)

nums = [0, 1, 2, 2, 3, 0, 4, 2]
solution = Solution()
k = solution.remove_element(nums, 2)

print(k)  # Expected output: 5
print(nums[:k])  # Expected output: [0, 1, 3, 0, 4]



"""
OPTIMAL SOLUTION

    def removeElement(self, nums: list[int], val: int) -> int:
        i = 0
        
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
                
        return i

"""