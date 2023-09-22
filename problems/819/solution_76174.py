def filtraMultiplos(listai,n):
    """Separa os números múltiplos de n em uma lista
       list,int ~> list"""
    listaf = []
    contador = 0
    while contador < len(listai):
        if listai[contador]%n == 0:
            list.append(listaf,listai[contador])
        contador += 1
    return listaf