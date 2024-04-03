class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        answer = []
        numsLeft = []
        numsRight = nums
        countLeft = 0
        countRight = numsRight.count(1)
        indexHolder = [countLeft + countRight]

        for x in range(len(nums)):
            numsLeft.append(numsRight[x])
            if numsRight[x] == 0:
                countLeft += 1
            countRight -= numsRight[x]
            indexAdd = countLeft + countRight
            indexHolder.append(indexAdd)

        large = max(indexHolder)
        for y in range(len(indexHolder)):
            if indexHolder[y] == large:
                answer.append(y)  
        return answer