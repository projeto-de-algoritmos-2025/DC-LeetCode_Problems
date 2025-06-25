from typing import List

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def merge_sort(start, end):
            if start >= end:
                return 0
            
            mid = (start + end) // 2
            count = merge_sort(start, mid) + merge_sort(mid + 1, end)
            
            # Conta pares onde nums[i] > 2 * nums[j]
            j = mid + 1
            for i in range(start, mid + 1):
                while j <= end and nums[i] > 2 * nums[j]:
                    j += 1
                count += j - (mid + 1)
            
            # Faz o merge ordenado
            temp = []
            left, right = start, mid + 1
            while left <= mid and right <= end:
                if nums[left] <= nums[right]:
                    temp.append(nums[left])
                    left += 1
                else:
                    temp.append(nums[right])
                    right += 1
            while left <= mid:
                temp.append(nums[left])
                left += 1
            while right <= end:
                temp.append(nums[right])
                right += 1
            nums[start:end+1] = temp
            return count

        return merge_sort(0, len(nums) - 1)
