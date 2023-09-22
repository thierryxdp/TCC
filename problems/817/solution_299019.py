def maiores(lista, n):
    '''
    Ao inserir a lista com números inteiros e um número inteiro, o código
    retorna a lista somente com os números maiores que o número inserido
    e em ordem crescente
    list, int -> list
    '''
    x = ([i for i in lista if i > n])
    return sorted (x)

def acima_da_media(lista2):
    '''
    Ao inserir a lista com números inteiros, o código
    retorna a lista das notas em ordem crescente e a média
    list -> list, int
    '''
    y = sum(lista2)/len(lista2)
    return maiores(lista2, y)