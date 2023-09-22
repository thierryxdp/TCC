def filtraMultiplos(lista,n):
    '''Dada uma lista de numeros, retorna uma lista contendo todos os 
    numeros divisiveis por N '''
    
    multiplos = ()
    proximo = 0
    while proximo < len(lista):
        if lista[proximo]%n=0:
        	multiplos = multiplos + (lista[proximo])
        proximo = proximo + 1
    return multiplos