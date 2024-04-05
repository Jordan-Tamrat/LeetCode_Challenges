class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        answer=nums
        for x in range(len(nums)):
            if nums[x] == target:
                return x
            else:
                answer.append(target)
                answer.sort()
                for x in range(len(answer)):
                    if nums[x]==target:
                        return x
                