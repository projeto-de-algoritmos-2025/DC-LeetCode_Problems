from typing import List

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        counts = [0] * n
        indexed_nums = list(enumerate(nums))  # (index, value)

        def merge_sort(start, end):
            if end - start <= 1:
                return indexed_nums[start:end]
            
            mid = (start + end) // 2
            left = merge_sort(start, mid)
            right = merge_sort(mid, end)

            merged = []
            j = 0  # pointer for right half
            for i in range(len(left)):
                while j < len(right) and right[j][1] < left[i][1]:
                    j += 1
                counts[left[i][0]] += j

            # Merge os dois arrays ordenadamente
            return sorted(left + right, key=lambda x: x[1])

        merge_sort(0, n)
        return counts
