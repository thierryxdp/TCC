def filtraMultiplos (lista, numero):
    indice = 0
    lista2 = []
    while indice <= len(lista):
        if lista[indice] % numero == 0:
            lista2.append(lista[indice])
        indice += 1
    return lista2