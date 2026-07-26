class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        newNum = nums1 + nums2
        newNum.sort()

        length = len(newNum)

        if length % 2 == 0:
            median = (newNum[length//2] + newNum[length//2 - 1]) / 2
        else:
            median = newNum[length//2]

        return median
        