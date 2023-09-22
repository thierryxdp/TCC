def filtraMultiplos(lista_num, num):
    '''
    	Funcao que recebe uma lista de numeros e um numero
        retornando outra lista contendo todos os elementos
        da lista original que foram divisiveis por n
        list, int -> list
    '''
    i = 0
    multiplos = []
    
    while i < len(lista_num):
        if lista_num[i] % num == 0:
            multiplos.append(i, lista_num[i])
            i += i
    return multiplos