from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def select(arr, k):
            if len(arr) <= 5:
                return sorted(arr)[k]
            
            # Dividir em grupos de 5 e pegar medianas
            medians = [sorted(arr[i:i+5])[len(arr[i:i+5]) // 2] for i in range(0, len(arr), 5)]
            
            # Recursivamente acha a mediana das medianas
            pivot = select(medians, len(medians) // 2)

            # Particiona o array
            lows = [el for el in arr if el < pivot]
            highs = [el for el in arr if el > pivot]
            pivots = [el for el in arr if el == pivot]

            if k < len(lows):
                return select(lows, k)
            elif k < len(lows) + len(pivots):
                return pivot
            else:
                return select(highs, k - len(lows) - len(pivots))
        
        return select(nums, len(nums) - k)  # <- Correção aqui
