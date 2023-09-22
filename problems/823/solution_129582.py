def faltante(lista):

    lista.sort()
    contador = 0
    adicionador = 0
    lista2 = []

    while contador < len(lista)-1:
        if lista[contador+1] - lista[contador] > 1:
            adicionador = lista[contador+1]-1
            lista2.append(adicionador)
        contador += 1

    if lista2 != []:
        return lista2[0]

    if lista[0] > 1:
        list.append(lista2, 1)

    if lista[0] == 1:
        list.append(lista2, lista[-1]+1)

    return lista2[0]