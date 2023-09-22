def filtraMultiplos(lista,n):
    '''função que recebe uma lista de números e um número (n) e retorna 
    outra lista contendo todos os elementos da lista original que forem 
    divisíveis por n. 
    list -> list''' 
    multiplos = [] 
    i = 0
    
    while i < len(lista):
        if lista[i] % n == 0:
            multiplos += [lista[i],]
        i += 1
    return multiplos