def diagonalDifference(arr):
    n = len(arr)
    a = b = 0

    for i in range(n):
        a += arr[i][i]
        b += arr[i][n - 1 - i]

    return abs(a - b)


if __name__ == '__main__':
    n = int(input().strip())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))

    print(diagonalDifference(arr))
