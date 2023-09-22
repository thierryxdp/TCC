def filtraMultiplos(lista, n):
    """Retorna uma lista com todos os elementos da lista original divisíveis por n; lista, int -> lista."""
    i = 0
    lista2= lista[:]
    novalista=[]
    while i < len(lista):
        if lista2[i:(i+1):]%n == 0:
            novalista = novalista+lista[i:(i+1):]
    return novalista