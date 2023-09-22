def faltante(seq):
    ref = [item for item in range(1, max(seq) +1)]
    diferenca = [item for item in ref if item not in seq]
    return diferenca