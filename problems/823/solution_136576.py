def faltante(n):
    i = 0
    peca = 0
    list.sort(n)
    while n[i] == n[i-1] + 1:
        peca = n[-1] + 1        
        i += 1
    if not n[i] == n[i-1] + 1
    return peca