def faltante(pecas):
    list.sort(pecas)
    c = 1
    while c < len(pecas) + 2:
        if c not in pecas:
            return c
        c += 1