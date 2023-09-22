def maiores(lista,n):
    '''
        Funçao que dada uma lista de numeros inteiros e um numero inteiro n, retorna
        outra lista, que contenha todos os numeros da lista original maiores que n
        ordenados em ordem crescente
        lista = list.
        n = int.
        return = list.
    '''
    x = sorted(lista)
    if x[0] > n:
     return x
    elif x[1] > n:
        return x[1:]
    elif x[2] > n:
        return x[2:] 
    elif x[3] > n:
        return x[3:]
    elif x[4] > n:
        return x[4:]
    elif x[5] > n:
        return x[5:]
    elif x[6] > n:
        return x[6:]
    else:
        return list.clear(x)