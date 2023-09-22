def fatorial(numero):
    ''' Função que dado um número inteiro qualquer, retorna
    o fatorial desse número.
    Entrada: int
    Retorno: int '''

    lista_numeros = list(range(1,numero+1))
    indice = 1
    multiplicacao = 1
    while indice < len(lista_numeros):
        multiplicacao = multiplicacao * (lista_numeros[indice])
        indice = indice + 1
                                         
    return multiplicacao