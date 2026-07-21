class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            for j in range (len(matrix[i])):
                val = matrix[i][j]
                if val == target:
                    return True
        return False