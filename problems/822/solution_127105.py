def repetidos(lista):
    i=lista
    if i[0] in lista:
        return lista.count(i[0])
    if i[9] in lista and i[12] in lista:
        return lista.count(i[9])+ lista.count(i[12])