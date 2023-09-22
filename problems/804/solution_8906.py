def filtra_pares(p):
    n=()
    if p[0] %2 == 0:
        return n== n+(p[0],)
    if p[1] % 2 == 0:
        return n== n+(p[0:1],)
    if p[2] % 2 == 0:
        return n== n+(p[0:2],)
    if p[3] % 2 == 0 :
        return n== n+(p[0:3],)
    return n