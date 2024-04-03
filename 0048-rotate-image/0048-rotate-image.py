class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        for i in range(len(matrix)):
            for j in range(i,len(matrix)):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        for i in range(len(matrix)):
            x = 0
            y = len(matrix) - 1
            while x < y:
                matrix[i][x], matrix[i][y] = matrix[i][y], matrix[i][x]
                x += 1
                y -= 1
        return matrix

