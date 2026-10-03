def pairInSortedRotated(arr, target):
    n = len(arr)

    if n < 2:
        return False

    smallest = 0
    for i in range(1, n):
        if arr[i] < arr[smallest]:
            smallest = i

    left = smallest
    right = (smallest - 1 + n) % n

    while left != right:
        total = arr[left] + arr[right]

        if total == target:
            return True
        elif total < target:
            left = (left + 1) % n
        else:
            right = (right - 1 + n) % n

    return False

if __name__ == '__main__':
    arr = list(map(int, input().split()))
    target = int(input())
    print(pairInSortedRotated(arr, target))
