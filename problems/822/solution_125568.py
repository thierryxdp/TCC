def repetidos(nums):
    ocorrencias = []
    for c in nums:
        if c in ocorrencias:
            ocorrencias[c] = ocorrencias[c] + 1
    return ocorrencias.count(1,2,3,4,5,6,7,8,9)