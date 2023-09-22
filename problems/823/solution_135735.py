def faltante(n):
    i = 1
    peca = 0
    list.sort(n)
    while i < len(n):
        if not n[i-1] == n[i] - 1:
            peca = n[i-1] + 1
        i += 1
    return peca