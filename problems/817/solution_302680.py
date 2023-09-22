def maiores(x, n):
    '''a função redece uma lista de numeros inteiros e um numero inteiro n e retorna outra lista contendo os numeros da lista original maiores que n e ordenados em ordem crescente
    assinatura: list(int) int -> list(int)
    '''
    x = list.append(x, n)
    z = []
	n = 5
    for y in x:
        if y >= n:
            list.append(z, y)
    list.sort(z)
    return z

def acima_da_media(x):
    '''a funcao recebe uma list com notas e retorna uma lista ordenada com as notas que ficaram acima da media
    assinatura: list(int) -> list(int)
    '''
    x = maiores(x)