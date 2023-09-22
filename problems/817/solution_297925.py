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
    '''...
    list->list'''
    
    lista = maiores(lista)
    
    return lista