def filtraMultiplos (lista, numero):
    '''dada uma lista de numeros e um numero, retorna uma lista contendo os multiplos do numero pertencentes a lista original
       : list, int -> list
    '''
    i = 0
    multiplos = []
    
    while i < len(lista):
        if lista[i]%numero == 0:
            multiplos = multiplos + lista[i]
        i = i+1
    return multiplos