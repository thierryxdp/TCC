def faltante(listaI):
    """Calcula e retorna o numero referante a peca do
    quebra cabeca que esta faltando no intervalo
    de um ate o total de pecas, dado uma lista
    com numero de paças igual ao numero de pecas total
    menos 1(nPecas), sem numeros repetidos; list, int"""
    i=1
    falta=0
    while i <= len(listaI):
        if i in listaI:
            falta = falta + 1
        i=i+1
    return falta + 1
i=1,3,4,5