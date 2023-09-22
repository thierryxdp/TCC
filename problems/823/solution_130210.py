def faltante(l):
    """Função que dada uma lista com N - 1 inteiros numerados de 1 a N (não repetidos), descobre qual numero entre 1 e N não esta na lista "l"
       Retorna o numero inteiro que pertence ao intervalo [1,n] mas que não pertence a lista de entrada fornecida
       list -> int"""
    n = len(l) + 1
    listaCompleta = range(1,n+1)
    indice = 0
    while indice < len(listaCompleta):
        if listaCompleta[indice] not in l:
            return listaCompleta[indice]
        indice += 1