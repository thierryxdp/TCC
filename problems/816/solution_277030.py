def maiores(lista,n):
    '''dada uma lista de números inteiros e um número inteiro n, retorna
    uma nova lista somente com os números da lista de entrada maiores que n;
    list, int -> list'''

    list.append(lista,n)
    list.sort(lista)
    lugar = list.index(lista,n)+1
    
    return lista[lugar:]