def maiores(acima_da_media,n):
    '''funçãoque dada uma lista de numeros inteiros e um numero inteiro n, retorna outra lista, que contenha todos os numeros da lista original maiores que n, ordenados em ordem crescente:
       list, int -> list'''
    l1=lista_numeros+[n]
    list.sort(l1)
    a=list.index(l1,n)
    return l1[a:]