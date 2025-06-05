class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        res = []
        for i in range(len(matrix)):
            row_min = min(matrix[i])
            col_idx = matrix[i].index(row_min)
            if all(matrix[r][col_idx] <= row_min for r in range(len(matrix))):
                res.append(row_min)
        return res
