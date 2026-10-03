def diagonalSort(mat):
    m, n = len(mat), len(mat[0])

    for k in range(m + n - 1):
        r = max(0, k - n + 1)
        c = max(0, n - 1 - k)

        a = []
        i, j = r, c

        while i < m and j < n:
            a.append(mat[i][j])
            i += 1
            j += 1

        a.sort()

        i, j = r, c
        for x in a:
            mat[i][j] = x
            i += 1
            j += 1

    return mat
if __name__ == '__main__':
    m, n = map(int, input().split())
    mat = []
    for i in range(m):
        mat.append(list(map(int, input().split())))

    print(diagonalSort(mat))
