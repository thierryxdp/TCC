def maiores(lista,m):
    '''função que dada uma lista de números inteiros e um número inteiro (n), retorna outra lista, que contenha todos os números da lista original maiores que (n), ordenados em ordem crescente; list, int -> list'''
    list.append(lista,m)
    list.sort(lista)
    p=list.index(lista,m)
    return lista[p+1:]
    
def acima_da_media(lista):
    m=int((sum(lista))/(len(lista)))
    list.remove(lista,m)
    return maiores(lista,m)  
acima_da_media([1,2,3,4])