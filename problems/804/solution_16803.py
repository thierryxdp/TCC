def par(x):
    return x%2==0
def filtra_pares(tupla):
    """Ao receber a tupla com quatro elementos, retornar uma tupla contento apenas os pares"""
    filtro=()
    if par(tupla[0]):
        filtro= filtro+ (tupla[0],)
    if par(tupla[1]):
        filtro= filtro + (tupla[1],)
    if par(tupla[2]):
        filtro= filtro + (tupla[2],)
    if par(tupla[3]):
        filtro= filtro + (tupla[3],)
    return filtro