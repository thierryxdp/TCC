def conta_numero(n,mat):
    """doc"""
    qntd = 0
    for linha in mat:
        for elem in linha:
            qntd += 1 if n == elem in linha else 0
    return qntd