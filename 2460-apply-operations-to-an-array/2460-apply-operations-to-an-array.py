class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for x in range(len(nums)-1):
            if nums[x] != nums[x + 1]:
                nums[x]=nums[x]
            elif nums[x] == nums[x + 1]:
                nums[x]=nums[x] * 2
                nums[x+1]=nums[x + 1] * 0
        for x in range(len(nums)):
            if nums.count(0):
                nums.remove(0)
                nums.append(0)
        return nums
                
