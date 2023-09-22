def filtraMultiplos(listai,n):
    """Separa os números múltiplos de n em uma lista
       list,int ~> list"""
    listaf = []
    contador = 0
    while contador < len(listai):
        if int(listai[contador])%int(n) == 0:
            listaf += listai[contador]
        contador += 1
    return listaf