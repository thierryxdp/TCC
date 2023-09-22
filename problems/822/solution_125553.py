def repetidos(lista):
	pos = 0 #contador
    vezes = [] #acumulador
    while pos < len(lista):
        if lista[pos] in lista[:pos]:
            vezes = list.append(lista, lista[pos])
        pos = pos + 1
    return vezes