class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1

        target_row = None
        while l <= r:
            mid = (l + r) // 2

            if target < matrix[mid][0]:
                r = mid - 1
            elif target > matrix[mid][-1]:
                l = mid + 1
            else:
                target_row = matrix[mid]
                break

        if target_row is None:
            return False
        l = 0
        r = len(target_row) - 1
        while l <= r:
            mid = (l + r) // 2

            if target_row[mid] < target:
                l = mid + 1
            elif target_row[mid] > target:
                r = mid - 1
            else:
                return True
        return  False             

            