def melhor_volta(matriz):
    contador = 0
    contador2 = 0
    lista = []
    for i in range(6):
        for j in range(10):
            lista.append(min(matriz))
            if lista[i] not in matriz[i]:
                contador += 1
            else:
                contador += 0
	contador2 += list.index(matriz[contador],(min(lista)))
    return (contador2,min(lista),contador)