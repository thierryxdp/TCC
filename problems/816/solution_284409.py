def maiores(lista_numero,n):
    '''dada uma lista de numeros inteiros e um numero inteiro n, retorna outra lista, que contenha
todos os numeros da lista original maiores que n ordenados em ordem crescente.list,int->list'''
    segunda_lista = []
    soma = 0

    for x in lista_numero:
        if x >= n:
            segunda_lista.append(x)

    for x in segunda_lista:
        soma += x
     
    ordenada = list.sort(segunda_lista)
    return segunda_lista