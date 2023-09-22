def faltante(lista):
    lista.sort()
    cont = 1 
    while (cont-1 < len(lista)):
        if lista[cont-1] != cont:
            return cont
        cont = cont + 1
    return len(lista)