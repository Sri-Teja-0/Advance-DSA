'''yr#48 Rotate Image
from typing import List
def rotate(mat: list[list[int]]) -> None:
    n = len(mat)
    for i in range(n):
        for j in range(i+1,n):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
    for row in mat:
        row.reverse()
mat = [[1,2,3],[4,5,6],[7,8,9]]
rotate(mat)
print(mat)'''

# 1886 Determine Whether Matrix Can Be Obtained By Rotation
from typing import List
def findRotation(mat: List[List[int]], target: List[List[int]]) -> bool:
    n = len(mat)
    for i in range(4):
        if mat == target:
            return True
        for i in range(n):
            for j in range(i+1, n):
                mat[i][j], mat[j][i] = mat[j][i],mat[i][j]
        for row in mat:
            row.reverse()
    return False
mat = [[0,1],[1,0]]
target = [[1,0],[0,1]]
print(findRotation(mat, target))