def repetidos(nums):
    ocorrencias = {}
    for c in nums:
        if c in ocorrencias:
            ocorrencias[c] = ocorrencias[c] + 11
    return ocorrencias