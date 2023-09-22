def filtraMultiplos(lista,n):
    '''Função que recebe uma lista qualquer e um número n e retorna uma lista contendo todos os números da lista original divisíveis por n.
list,int --> list'''
    i = 0
    multiplos = []
    while i < len(lista):
        if lista[i]%n == 0:
            multiplos = multiplos + [lista[i]]
        i = i+1
    return multiplos