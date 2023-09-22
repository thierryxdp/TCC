def repetidos(nums):
    ocorrencias = []
    ocorrenciasdup = []
    for c in nums:
        if c in ocorrencias:
            ocorrenciasdup[c] = ocorrencias[c] + 1
            x = ocorrenciasdup
        else:
            ocorrencias[c] = 1  
    return x