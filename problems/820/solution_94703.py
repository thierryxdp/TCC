def posLetra(texto,letra,num):
    i = 0
    cont = 0
    while i < len(texto)-1:
        if texto[i] == letra:
            cont = cont + 1
        if cont == num:
            return i
        i = i + 1
    return -1