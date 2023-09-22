def faltante(lista):
    lista.sort()
    cont = 1 
    while (cont-1 < len(lista)):
        if lista[cont-1] != cont:
            saida = cont
        cont = cont + 1
    return saida