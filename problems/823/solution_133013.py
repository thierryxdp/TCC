def faltante(lista):
    list.sort(lista)
    n = len(lista)
    lista2 = list.range(n)
    i = 0
    resposta = 0
    while i<len(lista):
        if lista[i] != lista1[i]:
            resposta = lista1[i]
        i = i + 1
    return resposta