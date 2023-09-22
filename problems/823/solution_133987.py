def faltante(lista):
    i = 0
    opa = range(1, len(lista)+1)
    while i < len(lista):
        if lista[i] != opa[i]:
            return opa[i]
        i = i + 1