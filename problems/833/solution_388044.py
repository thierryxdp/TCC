def conta_numero(numero,matriz):
    '''Função que dado um numero inteiro e uma matriz, conta e retorna quantas vezes aquele numero aparece na matriz.
    int, list -> int'''
    contador = 0
    for quantidade in matriz:
        qtd = list.count(quantidade,numero)
        contador = contador + qtd
    return contador