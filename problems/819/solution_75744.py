def filtraMultiplos (lista,n):
    """ a função recebe uma 'lista' e um número 'n' e retorna outra lista
    contendo todos os elementos da lista original que forem divisíveis por 'n'.
    list, int -> list """
    multiplos = []
    i=0
    
    while lista[i]%n == 0:
        multiplos += [lista[i]]
        i = i + 1
        
    return multiplos