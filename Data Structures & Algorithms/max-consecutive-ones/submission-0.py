class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = 0
        maxConsecOnes = 0
        for num in nums:
            if num == 1:
                counter += 1
                print(counter)
            else:
                if maxConsecOnes <= counter:
                    maxConsecOnes = counter
                counter = 0
        if maxConsecOnes <= counter:
                    maxConsecOnes = counter
        return maxConsecOnes

