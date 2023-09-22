def maiores (lista, n):
    '''Funcao que, dada uma lista de numeros inteiros e um numero inteiro n, retorna outra
lista, que contenha todos os números da lista original maiores que n,
list, int -> list'''


    if n in lista:
        L = list.index (lista,n)
        return lista[L+1 :]

    if n not in lista:
        lista.append (n) 
        list.sort (lista)
        L1 = list.index (lista, n)
        return lista[L1+1:]