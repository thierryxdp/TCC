def faltante(L):
    '''Funcao que recebe uma lista e um numero com N-1 inteiros(nao repetidos), listados
de 1 a N, retornando o numero inteiro x que pertence ao intervalo [1,N] mas que
nao pertence a lista de entrada L'''
    listaNumerada = list(range(1,len(L)+1))
    list.sort(L)
    contador = 0
    contadorNumerada = 0
    while contadorL < len(L):
        if listaNumerada[-1] == L[-1]+1:
            return listaNumerada[-1]
        if L[contador] == listaNumerada[contador]:
            indice += 1
        else:
            return listaNumerada[contador]