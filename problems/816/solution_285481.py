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
    if lista[0] > n:
     return x
    elif lista[1] > n:
        return x[1:]
    elif lista[2] > n:
        return x[2:] 
    elif n > lista:
        return list.clear(lista)
    elif lista[3] > n:
        return x[3:]
    elif lista[4] > n:
        return x[4:]
    elif lista[5] > n:
        return x[5:]
    elif lista[6] > n:
        return x[6:]