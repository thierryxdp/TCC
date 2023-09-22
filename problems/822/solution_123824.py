def repetidos(nums):
    ocorrencias = {}
    ocorrenciasdup = {}
    for c in nums:
        if c in ocorrencias:
            ocorrenciasdup[c] = ocorrenciasdup[c] +1
        else:
            ocorrencias[c] = 1  
    return x