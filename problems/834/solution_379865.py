def media_matriz(m):
    zeros = 0
    for linha in m:
        for aij in linha:
            if aij == 0:
                zeros = zeros + 1
    total = len(m)*len(m[0])
    return (total - zeros) / total