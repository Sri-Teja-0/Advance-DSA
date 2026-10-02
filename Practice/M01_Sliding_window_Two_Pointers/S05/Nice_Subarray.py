"""1248 Count Number of Nice Subarrays
from typing import List
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i] %= 2
        prefix_count = [0] * (len(nums) + 1)
        prefix_count[0] = 1
        s = 0
        ans = 0
        for num in nums:
            s += num
            if s >= k:
                ans += prefix_count[s - k]
            prefix_count[s] += 1
        return ans
if __name__ == "__main__":
    nums = [1, 1, 2, 1, 1]
    k = 3
    print(Solution().numberOfSubarrays(nums, k))  # Output: 2
"""

#1763 Longest Nice Subarray

def longestNiceSubstring(s: str) -> str:
    if len(s) < 2:
        return ""

    char = set(s)

    for i in range(len(s)):
        if s[i].swapcase() not in char:

            left = longestNiceSubstring(s[:i])
            right = longestNiceSubstring(s[i+1:])

            if len(left) >= len(right):
                return left
            else:
                return right

    return s  
s1 = "YazaAay"
s2 = "Bb"
s3 = "c"
print(longestNiceSubstring(s1))  # Output: "aAa"
print(longestNiceSubstring(s2))  # Output: "Bb"
print(longestNiceSubstring(s3))  # Output: "c"