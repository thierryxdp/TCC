def faltante(lista):
    
    tam_da_lista = len(lista) + 1
    N = 1
    pecas = [N]
    
    while N < tam_da_lista:
        pecas += [(N+1),]
        N = N + 1
    totalObservado = sum(lista)
    totalEsperado = sum(pecas)
    
    return totalEsperado - totalObservado