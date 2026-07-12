class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for r in range(9):
            seen_in_row = set()
            current_row = board[r]
            for val in current_row:

                if val == '.':
                    continue
                if val in seen_in_row:
                    return False
                seen_in_row.add(val)

        for c in range(9):
            seen_in_col= set()
            for r in range(9):
                val = board[r][c]

                if val == '.':
                    continue
                if val in seen_in_col:
                    return False
                seen_in_col.add(val) 

        boxes = {}

        for r in range(9):
            for c in range (9):
                val = board [r][c]
                if val == '.':
                    continue

                box_key = (r // 3, c // 3)

                if box_key not in boxes:
                    boxes[box_key] = set()

                if val in boxes[box_key]:
                    return False
                boxes[box_key].add(val)                    
        return True