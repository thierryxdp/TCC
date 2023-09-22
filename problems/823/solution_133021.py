def faltante(lista):
    list.sort(lista)
    i = 1
    resposta = 0
    while i<len(lista):
        if lista[i] != i:
            resposta = i
        i = i + 1
    return resposta