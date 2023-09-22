def filtraMultiplos(lista,n):
    '''Função que recebe uma lista de números e um número e retorna outra lista contendo todos os elementos da lista original que forém divisíveis por n: list,int -> list'''
    i = 0
    while i < len(lista):
        if lista[i]%n == 0:
            print lista[i]
        i += 1
    return [lista]