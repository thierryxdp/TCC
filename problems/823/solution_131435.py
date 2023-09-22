def faltante(peças):
    N = len(peças + 1)
    completo = range(1, N, 1)
    indice = 0
    
    while indice < len(peças):
        if completo[indice] not in peças:
            return completo[indice]