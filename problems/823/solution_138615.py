def faltante(pecas):
    list.sort(pecas)
    c = 1
    while c < len(pecas) + 1:
        if c not in pecas:
            return c
        c += 1