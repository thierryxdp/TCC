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
    A = list.index(lista,n)
    return lista[A+1:]