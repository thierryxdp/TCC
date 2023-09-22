def faltante(lista):
    i=0
    if lista[0] is not 1:
        return 1
    else:
        while i<lista[-1]:
                if i not in lista:
                    return i
                else:
                    i=i+1