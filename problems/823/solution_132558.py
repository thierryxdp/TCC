def faltante(lista_numeros):
    '''Função que recebe uma lista de tamanho N - 1 contendo números inteiros não repetidos de 1 a N.
    Retorna o número que pertence ao intervalo [1,N] mas que não pertence a lista de entrada;
    list -> int'''
    n = max(lista_numeros)
    soma1 = n*(n+1)//2
    soma2 = 0
    i = 0
    while i <len(lista_numeros):
        soma2 = soma2 + lista_numeros[i]
        i=i+1
    if soma2 != soma1:
        soma = soma1 - soma2
    else:
        soma = n+1
    return soma