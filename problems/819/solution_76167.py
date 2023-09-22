def filtraMultiplos(lista,n):
    """Separa os números múltiplos de n em uma lista
       list,int ~> list"""
    listaf = []
    contador = 0
    while contador < len(lista):
        if int(lista[contador])% n == 0:
            listaf = listaf + list(lista[contador])
        contador += 1
    return listaf