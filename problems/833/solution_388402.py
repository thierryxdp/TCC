def conta_numero(n, mat):
    c = 0
    for r in mat:
        for e in r:
            if e == n:
                c += 1
    return c