# original_solution/two_sum.py

def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

# Example usage
print(twoSum([2, 7, 11, 15], 9))  # Output: [0, 1]
