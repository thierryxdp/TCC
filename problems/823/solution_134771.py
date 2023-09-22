def faltante(lista):
    i = 0
    numeroQueFalta = 0
    list.sort(lista)
    numeroFinal = lista[-1] + 1
    numeroInicio = lista[0]
    parametro = list(range(numeroInicio,numeroFinal))
    while i < len(lista):
        if lista[i] != parametro[(i)]:
            numeroQueFalta = numeroQueFalta + parametro[(i)]
        else:
            numeroQueFalta = lista[0] - 1
        i = i + 1
    return numeroQueFalta