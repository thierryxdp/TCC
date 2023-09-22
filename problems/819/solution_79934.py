def filtraMultiplos(lista_num, n):
    '''
    	Funcao recebe uma lista de numeros e um numero
        e retorna outra lista contendo os elementos da 
        lista original que forem divisiveis por n.
        list(elementos int) -> int
        
    '''
    i = 0 
    divisiveis = []
    
    while i < len(lista_num):
        if lista_num[i]%n == 0:
            divisiveis = lista_num[i]
        i = i + 1
    return divisiveis