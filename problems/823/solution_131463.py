def faltante(pecas):
    N = len(pecas) + 2
    completo = range(1, N, 1)
    indice = 0
    
    while indice < len(completo):
        if completo[indice] in pecas:
            pass
        else:
            return completo[indice]
    
        indice += 1
    return completo[indice-1]