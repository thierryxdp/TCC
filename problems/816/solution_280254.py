def maiores(lista, n):
    '''função que dada uma lista de números inteiros e um número inteiro n, retorna outra lista que contenha todos os numeros da lista original maiores que n:list,int-> list'''
    if n not in lista : 
        list.append(lista,n)
    list.sort(lista)
    indice = list.index(lista,n)
    fatiado = lista[indice+1:]
    return fatiado