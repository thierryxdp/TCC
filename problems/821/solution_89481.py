def fatorial(n):
    '''Funcao que retorna o fatorial de um determinado numero n.
Int -> int'''
    fator = 1
    lista_fatores = [ ]
    while fator < n+1:
        lista_fatores = lista_fatores + [fator,]
        fator = fator + 1

    i = 0
    produto = 1
    while i < len(lista_fatores):
        produto = produto*(lista_fatores[i])
        i = i + 1
    return produto