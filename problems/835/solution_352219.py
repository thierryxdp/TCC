def melhor_volta(m):
    l = []
    for linha in range(len(m)):
        for coluna in range(len(m[0])):
            l.append(m[linha][coluna])
    a = min(l)
    for linha in range(len(m)):
        for coluna in range(len(m[0])):
            if m[linha][coluna] == a:
                b = linha + 1
                c = coluna + 1

    return (b,a,c)