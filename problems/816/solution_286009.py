def maiores (lista_numeros, n):
    '''retorna outra lista em ordem crescente com os números da lista dada (lista_numeros) maiores que o número n
    list, int -> list'''
    lista_nova = []
    contador = 0
    while contador < len(lista_numeros):
        if lista_numeros[contador] > n:
            lista_nova.append(lista_numeros[contador])
    	contador += 1
    lista_nova.sort()
    return lista_nova