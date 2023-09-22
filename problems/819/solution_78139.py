def filtraMultiplos(lista,numero):
    divisiveis = []
    contador = 0
    while contador < len(lista):
        if lista[contador]%numero == 0:
            list.append(divisiveis,lista[contador])
        contador += 1
    return divisiveis