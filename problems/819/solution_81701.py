def filtraMultiplos (lista, numero):
    '''dada uma lista de numeros e um numero, retorna uma lista contendo os multiplos do numero pertencentes a lista original
       : list, int -> list
    '''
   
    multiplos = []
    
    for num in lista:
        if num%numero == 0:
            multiplos = multiplos + [num]
    return multiplos