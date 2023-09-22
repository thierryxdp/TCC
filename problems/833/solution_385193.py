def conta_numero(num, mat):
    i = 0
    for linha in mat:
        for coluna in linha:
            if coluna == num:
                i += 1
    return i