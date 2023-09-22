def par(x):
    return x%2==0
    
def filtra_pares(tupla):
    """Ao receber a tupla com quatro elementos, retornar uma tupla contento apenas os pares"""
    filtro=[]
    if par(tupla[0]):
        return filtro+ tupla[0:1]
    if par(tupla[1]):
        return filtro + tupla[1:2]
    if par(tupla[2]):
        return filtro + tupla[2:3]
    if par(tupla[3]):
        return filtro + tupla[3:]