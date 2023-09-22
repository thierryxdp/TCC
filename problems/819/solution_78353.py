def filtraMultiplos(lista:list, numero) -> lista:
    '''dada uma lista e um número, retorna uma outra lista contendo
    todos os elementos da lista original que forem divisíveis por n'''
    i = 0
    multiplos = []
    while(i< len(lista)):
        if (lista[i]%numero == 0):
            multiplos = multiplos + lista[i]
        i=i+1
    return multiplos