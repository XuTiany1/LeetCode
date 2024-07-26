class Solution:
    
    def removeDuplicates(self, nums: list[int]) -> int:
        if(len(nums) == 0):
            return 0

        repeat_flag = False
        pointer = 1
        unique_value = nums[0]

        for current_value in nums[1:]:
                  
            if (current_value != unique_value):
                unique_value = current_value
                repeat_flag = False
                nums[pointer] = unique_value
                    
                pointer += 1
                
            elif (repeat_flag == False):
                repeat_flag = True
                nums[pointer] = current_value
                      
                pointer += 1

        return pointer


nums = [0,0,1,1,1,1,2,3,3]
solution = Solution()
k = solution.removeDuplicates(nums)

print(k)
print(nums)