def filtraMultiplos(lista):
    """Retorna uma lista com todos os elementos da lista original divisíveis por n; lista, int -> lista."""
    i = 0
    novalista=[]
    while i < len(lista[0]):
        if lista[0][i:(i+1):]%lista[1] == 0:
            novalista = novalista+lista[0][i:(i+1):]
        else:
            i= i +1
    return novalista