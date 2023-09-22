def repetidos(nums):
    ocorrencias = {}
    while c in nums:
        if c in ocorrencias:
            ocorrencias[c] = ocorrencias[c] + 1
        else:
            ocorrencias[c] = 1
    return ocorrencias[c]