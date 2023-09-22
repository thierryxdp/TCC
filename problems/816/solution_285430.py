def maiores(lista,n):
    '''
    função que dada uma lista de números inteiros e um número inteiro n, retorna outra lista que contenha todos os números da lista originals maiores que n, ordenados em ordem crescente;
    list, int - > list
    '''
    list.insert(lista,1,n)
    list.sort(lista)
    list.index(lista,n)
    nova_lista = lista[n+1:]
    return nova_lista