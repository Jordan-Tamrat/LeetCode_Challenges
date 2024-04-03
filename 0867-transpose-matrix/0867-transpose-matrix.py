class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        answer=[]
        x=0
        y=1
        for z in range(len(matrix[0])):
            a = []
            for i in range(len(matrix)):
                for j in range(x,y):
                    a.append(matrix[i][j])
            answer.append(a)
            x+=1
            y+=1
        return answer
        