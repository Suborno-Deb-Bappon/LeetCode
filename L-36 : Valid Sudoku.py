def duplicate_rows(matrix):
    for a in matrix:
        seen = set()
        for b in a:
            if b.isdigit() and b in seen:
                return True
            if b.isdigit():
                seen.add(b)
    return False 

def transpose(matrix):
    transposed_matrix = list(map(list, zip(*matrix)))
    return transposed_matrix
        
        
def duplicate_columns(matrix):
    t_matrix = transpose(matrix)
    for a in t_matrix:
        seen = set()
        for b in a:
            if b.isdigit() and b in seen:
                return True
            if b.isdigit():
                seen.add(b)
    return False   

def build_submatrix(matrix):
    submatrices = []
    for i in range(0,9,3):
        for j in range(0,9,3):
            submatrix = []
            for row in matrix[i:i+3]:
                 submatrix.append(row[j:j+3])
            submatrices.append(submatrix)
    return submatrices

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if(duplicate_rows(board) == False and duplicate_columns(board) == False):
            submatrices = build_submatrix(board)
            for submatrix in submatrices:
                if(duplicate_rows(submatrix) == True or duplicate_columns(submatrix) == True):
                    return False
            return True
        else:
            return False
                  
