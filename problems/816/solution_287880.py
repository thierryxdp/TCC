def maiores(lista,n):
    '''função que, dado uma lista de numeros inteiros e um numero inteiro n, retorna outra lista 
    que contenha todos os numeros da lista original maiores que n, ordenados em ordem crescente.
    list,int--->list'''
    list.append(lista,n)
    list.sort(lista)
    x=list.index(lista,n)
    return lista[x+1:]