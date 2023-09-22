def faltante(n):
    i = 0
    peca = 0
    list.sort(n)
    while i < len(n):
        if n[i] != n[i-1] + 1:
            peca = n[i] - 1
        i += 1
    return peca