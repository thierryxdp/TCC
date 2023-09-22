def faltante(pecas):
    lista = []
    i = 0
    while i in range(len(pecas)):
        lista.append(i+1)
        if not lista[i] in pecas:
            return lista[i]
        i = i + 1