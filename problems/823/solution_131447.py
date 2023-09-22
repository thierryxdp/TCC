def faltante(pecas):
    N = len(pecas) + 1
    completo = range(1, N, 1)
    indice = 0
    
    while indice < len(pecas):
        if completo[indice] in pecas:
            pass
        else:
            return completo[indice]
        
        indice += 1