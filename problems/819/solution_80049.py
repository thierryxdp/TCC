def filtra (lista,n):
    elem = len (lista)
    resposta = []
    contador = 0
    while elem > contador:
        if lista[contador]%n == 0:
            resposta += [lista[contador], ]
        contador += 1
    return resposta