def filtraMultiplos(lista,n):
    ''' função que dado uma lista de números e um
    número (n), retorna outra lista contendo todos os elemntos da
    lista original que forem divisíveis por n. list,int -> list.'''
    i = 0
    r = []
    while i < len(lista):
        if lista[i] % n == 0:
            r = r + [lista[i]]
            i = i + 1
            else:
                i = i + 1
    return r