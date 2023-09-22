def maiores (lista, n):
    '''Funcao que, dada uma lista de numeros inteiros e um numero inteiro n, retorna outra
lista, que contenha todos os números da lista original maiores que n,
list, int -> list'''

    if n in lista:
        L = list.index (lista,n)
        return lista[L+1 :]

    else :
        L1 = lista.append (n)
        L2 = list.sort (L1)
        L3 = list. index (L2, n)
        return lista[L3+1 :]