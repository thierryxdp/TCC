def repetidos(nums):
    ocorrencias = {}
    ocorrenciasdup = {}
    for c in nums:
        if c in ocorrencias:
            ocorrencias[c] = ocorrencias[c] + 1
        else:
            ocorrencias[c] = 1  
    return ocorrencias[c]