def maiores(lista,numero):
    copiaLista = lista[:]
    copiaLista2 = lista[:]
    if numero in lista:
        copiaLista.sort()
        indice = copiaLista.index(numero)
        novaLista = copiaLista[indice+1:]
        return novaLista
    elif numero not in lista:
        copiaLista2.append(numero)
        copiaLista2.sort()
        indice = copiaLista2.index(numero)
        nova = copiaLista2[indice+1:]
        return nova