def filtraMultiplos(lista_de_numeros,n):
    ''' função que recebe como entrada uma lista de números e
    	um número, e retorna outa lista contendo todos os
        multiplos de n
        list, int ---> list '''
    a = 0
    lista_multiplos = []
    while a < len(lista_de_numeros):
    	if lista_de_numeros[a] / n == int:
            lista_multiplos = list.append(lista_multiplos, lista_de_numeros[a])
        a += 1
    return lista_multiplos