def filtra_pares(w):
    if w[0]%2==0 and w[1]%2==0 and w[2]%2==0 and w[3]%2==0:
        return w[0], w[1], w[2], w[3]
    if w[0]%2==0 and w[1]%2==0 and w[2]%2==0:
        return w[0], w[1], w[2]
    if w[0]%2==0 and w[2]%2==0 and w[3]%2==0:
        return w[0], w[2], w[3]
    if w[0]%2==0 and w[1]%2==0 and w[3]%2==0:
        return w[0], w[1],w[3]
    if w[1]%2==0 and w[2]%2==0 and w[3]%2==0:
        return w[1], w[2], w[3]
    if w[0]%2==0 and w[1]%2==0:
        return w[0], w[1]
    if w[0]%2==0 and w[2]%2==0:
        return w[0], w[2]
    if w[0]%2==0 and w[3]%2==0:
        return w[0], w[3]
    if w[1]%2==0 and w[2]%2==0:
        return w[1], w[2]
    if w[1]%2==0 and w[3]%2==0:
        return w[1], w[3]
    if w[2]%2==0 and w[3]%2==0:
        return w[2], w[3]
    if w[3]%2==0:
        return w[3],
    if w[0]%2!=0 and w[1]%2!=0 and w[2]%2!=0 and w[3]%2!=0:
        return ()