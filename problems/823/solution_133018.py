def faltante(lista):
    list.sort(lista)
    i = 0
    n = 1
    resposta = 0
    while i<len(lista):
        if lista[i] != n:
            resposta = n
        i = i + 1
        n = n + 1
    return resposta