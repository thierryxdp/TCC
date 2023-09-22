def fatorial(numero):
    ''' Função que dado um número inteiro qualquer, retorna
    o fatorial desse número.
    Entrada: int
    Retorno: int '''

    from math import prod

    lista_numeros = list(range(1,numero+1))

    return math.prod(lista_numeros)