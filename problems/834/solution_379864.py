def media_matriz(m):
    total = 0
    zeros = 0
    for linha in m:
        for aij in linha:
            total = total + 1
            if aij == 0:
                zeros = zeros + 1
    return (total - zeros) / total