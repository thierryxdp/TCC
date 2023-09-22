def faltante(n):
    i = 0
    peca = 0
    list.sort(n)
    while i < len(n):
        if not n[i] == n[i-1] + 1:
            peca = n[i] - 1
        elif n[-1] == len(n):
            peca = n[-1] + 1
        i += 1
    return peca