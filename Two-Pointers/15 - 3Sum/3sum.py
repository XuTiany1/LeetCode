
def threeSum(self, nums: List[int]) -> List[List[int]]:

    # Step 1: Sort the array to use two-pointer technique
    nums.sort()
    result = []

    # Step 2: Loop through the array, fixing one number at a time
    for i in range(len(nums) - 2):
        # Skip duplicate elements to avoid duplicate triplets
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        # Use two pointers: one starting right after the fixed element, and one at the end
        left = i + 1
        right = len(nums) - 1

        # Step 3: Find pairs that together with nums[i] sum up to zero
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]

            if current_sum == 0:
                # Add the triplet to the result list
                result.append([nums[i], nums[left], nums[right]])
                # Move both pointers to the next different numbers
                left += 1
                right -= 1
                # Skip duplicates for left pointer
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                # Skip duplicates for right pointer
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif current_sum < 0:
                # If the sum is less than zero, move the left pointer to increase the sum
                left += 1
            else:
                # If the sum is greater than zero, move the right pointer to decrease the sum
                right -= 1

    return result

















