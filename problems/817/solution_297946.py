def maiores(lista,n):
    '''Dada uma lista numérica e um número inteiro, a função 
    retorna outra lista somente com os números da lista original de 
    ordem crescente
    list, int->list'''
    
    list = lista
    list.append(n)
    list.sort()
    list = list[(list.index(n)+1):]
    
    return list

def acima_da_media(lista):
    '''...'''
    
    lista1 = sum(lista)
    lista2 = len(lista)
    lista3 = lista1/lista2
    
    maiores(lista3)
    return lista