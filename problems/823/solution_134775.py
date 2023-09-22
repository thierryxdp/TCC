def faltante(lista):
    i = 0
    numeroQueFalta = 0
    numeroQueFaltaComIncio1 = 0
    list.sort(lista)
    numeroFinal = lista[-1] + 1
    numeroInicio = lista[0]
    parametro = list(range(numeroInicio,numeroFinal))
    while i < len(lista):
        if lista[i] != parametro[(i)]:
            return numeroQueFalta + parametro[(i)]
        else:
            if lista[0] != 1:
                return lista[0] - 1
            if lista[0] == 1:
                numeroQueFaltaComIncio1 = lista[-1] + 1
        i = i + 1
    return numeroQueFaltaComIncio1