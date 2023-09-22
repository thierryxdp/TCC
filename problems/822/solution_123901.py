def repetidos(nums):
    ocorrencias = {}
    for c in nums:
        if c in ocorrencias:
            ocorrenciaskek[c] = ocorrencias[c] + 1
        else:
            ocorrencias[c] = 1
    return ocorrenciaskek[c]