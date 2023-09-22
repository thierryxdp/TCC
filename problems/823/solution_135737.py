def faltante(n):
    i = 0
    peca = 0
    list.sort(n)
    list.append(n,n[-1]+1)
    while i < len(n):
        if not n[i-1] == n[i] - 1:
            peca = n[i-1] + 1
        i += 1
    return peca