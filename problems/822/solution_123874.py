def repetidos(nums):
    ocorrencias = {}
    for c in nums:
        if c in ocorrencias > 1:
            ocorrencias[c] = ocorrencias[c] + 1
        else:
            ocorrencias[c] = 1
    return ocorrencias