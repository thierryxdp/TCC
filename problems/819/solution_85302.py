def Multiplo(y,n):
    """ retorna se y é multiplo de n"""
    if y%n == 0:
        return 'true'
    else:
        return 'false'
def filtraMultiplos(lista,n):
    """ Recebe uma lista de números e um número n. Ela retorna os números dessa
lista que são múltiplos de n"""
    R = []
    for e in lista:
        if Multiplo(e,n) == 'true' :
          list.append(R,e)
    return R