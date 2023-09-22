def media_matriz(m):
    total = 0
    for linha in m:
        for aij in linha:
            total += 1
    return total