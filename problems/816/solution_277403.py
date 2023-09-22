def maiores(lista_numero,n):
    '''função que dada uma lista de números inteiros e um número inteiro n, calcula e retorna outra lista contendo todos os valores da lista original maiores que n
    list,int->list'''
    lista = lista_numero + [n] 
    list.sort(lista)
    x = list.index(lista,n)
    y = list.count(lista,n)
    
    return lista[x + y:]