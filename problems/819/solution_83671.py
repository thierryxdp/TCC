def filtraMultiplos (lista, n):
    '''
    função que recebe uma lista e um número n e retorna uma lista 
    com os números da lista original que são divisíveis por n
    '''
    lista_multiplos = []
    proximo = 0
    
    while proximo < len(lista):
        if lista[proximo] % n==0:
            lista_multiplos = lista_multiplos + [lista[proximo]]
        proximo = proximo + 1
    return lista_multiplos