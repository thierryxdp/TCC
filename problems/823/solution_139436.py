def faltante(lista):
    i=0
    if lista[0] is not 1:
        return 1
    else:
        while i<lista[-1]:
                if lista[i] not in lista:
                    return lista[1]
                else:
                    i=i+1