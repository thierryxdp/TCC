def acima_da_media(lista_numeros):
    '''funçãoque dada uma lista de numeros inteiros e um numero inteiro n, retorna outra lista, que contenha todos os numeros da lista original maiores que n, ordenados em ordem crescente:
       list, int -> list'''
    f1=sum(lista_numeros)/len(lista_numeros)
    f2= lista_numeros+[f1]
    list.sort(f2)
    a=list.index(f2, f1)
    return f2[a:]