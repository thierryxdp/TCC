def repetidos(nums):
    ocorrencias = {}
    ocorrenciasdup = {}
    for c in nums:
        if c in ocorrencias:
            ocorrenciasdup[c]
        else:
            ocorrencias[c] = 1  
    return ocorrenciasdup[c]