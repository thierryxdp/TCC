def maiores(numeros,n):
    '''função chamada maiores que dada uma lista de números inteiros
e um número inteiro n, retorne outra lista, que contenha todos os
números da lista original maiores que n, ordenados em ordem crescente
list,int->list'''
    list.append(numeros,n)
    list.sort(numeros)
    eliminar=list.index(numeros,n)
    eliminado=eliminar+1
    maioresN=numeros[eliminado:]
    return maioresN