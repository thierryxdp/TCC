def repetidos(nums):
    ocorrencias = {}
    for c in nums:
        if c in ocorrencias:
            ocorrenciasdup = ocorrencias[c] + 1
        else:
            ocorrencias[c] = 1
    return ocorrenciasdup