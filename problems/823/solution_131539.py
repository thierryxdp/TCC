def faltante(L):
    '''Funcao que recebe uma lista e um numero com N-1 inteiros(nao repetidos), listados
de 1 a N, retornando o numero inteiro x que pertence ao intervalo [1,N] mas que
nao pertence a lista de entrada L'''
    contador = 0
    tamanho = len(L)
    listaNumerada = list(range(1,tamanho+1))
    list.sort(L)
    while contador < len(L):
        if listaNumerada[-1] == L[-1]+1:
            return listaNumerada[-1]
        if L[contador] == listaNumerada[contador]:
            contador += 1
        else:
            return listaNumerada[contador]