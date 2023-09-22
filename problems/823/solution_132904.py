def faltante(lista):
    i = 0
    resultado = 0
    while i < len(lista)+1:
        if lista[i] != lista[i-1] + 1:
            resultado = lista[i]
            i = i+1
        else:
            i = i+1
    return resultado