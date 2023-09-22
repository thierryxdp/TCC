def maiores(lista,n):
    '''
        Funçao que dada uma lista de numeros inteiros e um numero inteiro n, retorna
        outra lista, que contenha todos os numeros da lista original maiores que n
        ordenados em ordem crescente
        lista = list.
        n = int.
        return = list.
    '''
    sorted(lista)
    if lista[0] > n:
     return lista
    elif lista[1] > n:
        return lista[1:]
    elif lista[2] > n:
        return lista[2:] 
    elif lista[3] > n:
        return lista[3:]
    elif lista[4] > n:
        return lista[4:]
    elif lista[5] > n:
        return lista[5:]
    elif lista[6] > n:
        return lista[6:]