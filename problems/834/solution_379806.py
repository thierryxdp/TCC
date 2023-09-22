def media_matriz(m):
    l = []
    for linha in range(len(m)):
        for coluna in range(len(m[0])):
            l.append(m[linha][coluna])
    return sum(l)/len(l)2]