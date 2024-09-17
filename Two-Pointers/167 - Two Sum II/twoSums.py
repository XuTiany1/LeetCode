class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        left_pointer = 0
        right_pointer = len(numbers) - 1

        curr_sum = numbers[left_pointer] + numbers[right_pointer]

        while(left_pointer < right_pointer):

            if(curr_sum == target):
                return [left_pointer+1, right_pointer+1]

            elif(curr_sum <= target):
                left_pointer =  left_pointer + 1
            
            else:
                right_pointer = right_pointer - 1
            
        
        