def faltante(L):
    i = 0
    opa = sorted(lista)
    while i < len(lista):
        if lista[i] != opa[i]:
            return lista[i] + 1
        i = i + 1