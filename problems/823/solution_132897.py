def faltante(lista):
    len(lista) = n - 1
    lista1 = list.append(lista1, lista)
    len(lista1) = n
    i = 0
    resultado = 0
    while i < len(lista1):
        if lista1[i] != lista[i-1] + 1:
            resultado = lista1[i]
        else:
            i = i+1
    return resultado