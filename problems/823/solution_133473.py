def faltante(pecas):
    "retorna um número inteiro x que pertence a um determinado intervalo mas que não se encontra na lista de entrada".
    list.sort(pecas)

    if pecas[0] != 1:
        return 1
    lista = list(range(pecas[0],pecas[-1]+1))
    if lista == pecas:
        return pecas[-1] + 1
    i = 0
    while i < len(lista):
        if lista[i] != pecas[i]:
            return lista[i]
        i = i+1
    else:
        return i-1