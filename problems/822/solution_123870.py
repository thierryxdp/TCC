def repetidos(nums):
    ocorrencias = {}
    for c in nums:
        if c in ocorrencias:
            ocorrencias[c] = ocorrencias[c] + 1
        else:
            ocorrencias[c] = 0
    return ocorrencias