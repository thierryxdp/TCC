def repetidos(nums):
    ocorrencias = {}
    for c in nums:
        if c in ocorrencias:
            ocorrencias[c] = ocorrencias[c] + 1
            x = ocorrencias
        else:
            ocorrencias[c] = 1  
    return x