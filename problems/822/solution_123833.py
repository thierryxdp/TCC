def repetidos(nums):
    ocorrencias = {}
    ocorrenciasdup = {}
    for c in nums:
        if c in ocorrencias:
            ocorrenciasrep = ocorrencias[c] + 1
            x = ocorrenciasrep
            sum(x)
        else:
            ocorrencias[c] = 1  
    return x