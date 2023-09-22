def maiores(lista, n):
    '''
    Ao inserir a lista com números inteiros e um número inteiro, o código
    retorna a lista somente com os números maiores que o número inserido
    e em ordem crescente
    list, int -> list
    '''
    x = ([i for i in lista if i > n])
    return sorted (x)