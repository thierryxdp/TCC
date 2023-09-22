def faltante(lista_numeros):
    '''Função que recebe uma lista de tamanho N - 1 contendo números inteiros não repetidos de 1 a N.
    Retorna o número que pertence ao intervalo [1,N] mas que não pertence a lista de entrada;
    list -> int'''
    n = max(lista_numeros)
    intervalo = list(range(1,n+1))
    numero = 0
    i = 0
    while i <len(intervalo):
        if intervalo[i] not in lista_numeros:
            numero = intervalo[i]
        elif intervalo[:] in lista_numeros:
            numero = n+2
        i=i+1
    return numero