def filtraMultiplos(lista, n):
    """Retorna uma lista com todos os elementos da lista original divisíveis por n; lista, int -> lista."""
    i = 0
    novalista=[]
    while i < len(lista):
        if lista[i:(i+1):]%n == 0:
            novalista = novalista+lista[i:(i+1):]
        else:
            i= i +1
    return novalista