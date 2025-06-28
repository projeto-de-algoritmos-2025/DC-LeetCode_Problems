class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        m, n = len(nums1), len(nums2)

        # se nums1 for maior que nums2, nós simplesmente chamamos a função de novo, trocando a ordem deles
        if m > n:
            return self.findMedianSortedArrays(nums2, nums1)

        # 'low' e 'high' definem o intervalo de ONDE podemos cortar o array nums1
        # cortes possiveis: primeiro elemento (0) ou último (m)
        low = 0
        high = m

        # +1 serve pra normalizar para arrays com numeros impares/pares
        half_len = (m + n + 1) // 2

        # busca o corte
        while low <= high:
            # tentativa de corte em nums1
            partition1 = (low + high) // 2

            # pegando o restante de nums2 para completar 'half_len'
            partition2 = half_len - partition1


            # olhando para os números que ficaram nas bordas do corte
            # 4 possibilidades:
            # maxLeft1: último número da parte esquerda de nums1
            # minRight1: primeiro número da parte direita de nums1
            # maxLeft2: último número da parte esquerda de nums2
            # minRight2: primeiro número da parte direita de nums2

            # se o corte for 0, não há nada na esquerda, então usamos -infinito
            maxLeft1 = nums1[partition1 - 1] if partition1 > 0 else -math.inf
            # se o corte for no final do array, não há nada na direita, então usamos +infinito
            minRight1 = nums1[partition1] if partition1 < m else math.inf

            # mesma coisa pra nums2
            maxLeft2 = nums2[partition2 - 1] if partition2 > 0 else -math.inf
            minRight2 = nums2[partition2] if partition2 < n else math.inf

            # o corte é ótimo se todos os números da esquerda forem menores ou iguais a todos os números da direita.
            # verificando bordas:
            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                # corte certo encontrado. Agora calcumaos a mediana
                total_len = m + n
                if total_len % 2 == 0:
                    max_of_left = max(maxLeft1, maxLeft2)
                    min_of_right = min(minRight1, minRight2)
                    return (max_of_left + min_of_right) / 2.0
                else:
                    return float(max(maxLeft1, maxLeft2))

            elif maxLeft1 > minRight2:
                # número da borda esquerda de nums1 é grande demais
                # 1. deveria estar mais para a metade direita
                high = partition1 - 1
            else: # maxLeft2 > minRight1
                # número da borda esquerda de nums2 é grande demais
                # 1. tentando o corte mais à direita da metade esquerda
                low = partition1 + 1