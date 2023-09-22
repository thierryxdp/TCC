def repetidos(nums):
    ocorrencias = {}
    for c in nums:
        if c in ocorrencias:
            ocorrenciasmult = ocorrencias[c] + 1
        else:
            ocorrencias[c] = 1
    return ocorrenciasmult