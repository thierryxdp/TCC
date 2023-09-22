def maiores(lista,n):
    '''dada uma lista de números inteiros e um número inteiro n, retorna
    outra lista, que contenha todos os números da lista original maiores
    que n. list,int->list'''
    if n not in lista:
        list.extend(lista,[n])
    else:
        lista=lista
    list.sort(lista)    
    Pn=list.index(lista,n)
    return lista[Pn+1:]