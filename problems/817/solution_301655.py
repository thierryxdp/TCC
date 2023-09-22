def acima_da_media(lista_numeros):
    '''funçãoque dada uma lista de numeros inteiros e um numero inteiro n, retorna outra lista, que contenha todos os numeros da lista original maiores que n, ordenados em ordem crescente:
       list, int -> list'''
    list.sort(lista_numeros)
    a=list.index(lista_numeros, sum(lista_numeros)/len(lista_numeros))
    return lista_numeros[a+1:]