def faltante(pecas):
    ''' Dados a lista de pecas retorna a peça faltante
    list -> int'''
    pecas.sort()
    len_pecas = len(pecas)

    if pecas[0] != 1:
        return 1
    if pecas[len_pecas -1] != (len_pecas + 1):
        return len_pecas

    i = 0
    while i < len_pecas:
        if not (pecas[i] + 1) == pecas[i + 1]:
            return pecas[i] + 1
        i+= 1