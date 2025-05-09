class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1): # Iterate over the list minus last element
            try:
                j = nums.index(target-nums[i],i+1) # Find the index of the target - nums[i] in the list starting from i+1 to avoice duplicates
                if i == j: # If the index is the same as the current index ignore it and continue to next index
                    continue

                return(i,j)
            except Exception as e: # Exception is raised when the index of target - nums[i] is not found, continue to next index
                continue
