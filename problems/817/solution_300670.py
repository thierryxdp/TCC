def maiores(lista,n):
    '''função que dada uma lista de números inteiros e um número
    inteiro n, retorna outra lista que contém todos os números da
    lista original maiores que n, ordenados em ordem crescente
    list,int -> list
    '''
    lista_maiores = list()
    inserir = lista.append(n)
    ordenar = lista.sort()
    i = lista.index(n)
    return lista[i+1:]
def acima_da_media(lista):
    soma = sum(lista)
    tam = len(lista)
    n = soma/tam
    return maiores(lista,n)