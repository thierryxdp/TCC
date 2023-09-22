def faltante(pecas):
    ''' Dados a lista de pecas retorna a peça faltante
    list -> int'''
    pecas.sort()

    i = 0
    while i < len(pecas):
        if not (pecas[i] + 1) == pecas[i + 1]:
            return pecas[i] + 1
        i+= 1