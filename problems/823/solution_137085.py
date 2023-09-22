def faltante (lista: int)-> int:
    '''Dada uma lista de tamanho N - 1 contendo inteiros (não repetidos)
    de 1 a N, retorna o número inteiro x que pertence ao intervalo [1,N],
    mas não pertence a lista de entrada L'''
    i = 0
    lista.sort()
    while i < len(lista):
        if lista[i] - 1 not in lista and lista[i]-1 !=0:
            return lista[i]-1
        i = i +1
    return lista [-1] + 1