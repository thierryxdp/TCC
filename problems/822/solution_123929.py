def repetidos(nums):
    ocorrencias = {}
    ocorrenciasdup = ' '
    for c in nums:
        if c in ocorrencias:
            ocorrenciasdup = ocorrencias + 1
        else:
            ocorrenciasdup = 1
    return ocorrenciasdup