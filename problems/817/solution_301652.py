def acima_da_media(lista_numeros):
    '''funçãoque dada uma lista de numeros inteiros e um numero inteiro n, retorna outra lista, que contenha todos os numeros da lista original maiores que n, ordenados em ordem crescente:
       list, int -> list'''
    n=sum(lista_numeros)
    l1=lista_numeros
    list.sort(l1)
    a=list.index(l1,n/len(l1))
    return l1[a+1:]