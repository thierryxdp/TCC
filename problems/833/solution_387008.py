def conta_numero(n,m):
    i = 0
    for linha in range(len(m)):
        for coluna in range(len(m[0])):
            if m[linha][coluna] == n:
                i = i + 1
    return i