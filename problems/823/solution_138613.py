def faltante(pecas):
    list.sort(pecas)
    c = 0
    while c < len(pecas) - 1:
        if c not in pecas:
            return c
        c += 1