def filtra_multiplos(lista_numeros,numero):
    ''' dados a lista de numeros e um numero, retorna os numeros da lista original
que forem multiplos do numero dado como 2° parametro de entrada
parametro de entrada: list,int retorno: list'''
    multiplos = []
    proximo = 0
    while proximo<len(lista_numeros):
        if lista_numeros[proximo]%numero==0:
            multiplos = multiplos + [lista_numeros[proximo]] 
        proximo= proximo + 1

    return multiplos