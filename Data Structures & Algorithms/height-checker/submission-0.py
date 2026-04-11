class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected_heights=sorted(heights)
        count=0

        for a,b in zip(heights, expected_heights):
            if a!=b:
                count+=1
        return count