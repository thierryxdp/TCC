def faltante(L):
    ''' Dada uma lista de tamanho N-1, retorna um numero
    inteiro x que pertence ao intervalo [1,N] mas que nao
    pertence a lista de entrada
    list -> int'''
    contador=1
    L.sort()
    while contador-1 < len(L):
        if L[contador] != L[(contador-1)] + 1:
            return contador
        contador +=1