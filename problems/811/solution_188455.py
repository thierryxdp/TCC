def colchao(medidas,H,L):
    if int(medidas[0]) <= int(L):
        return bool(True)
    if int(medidas[0]) <= int(H):
        return bool(True)
    if int(medidas[2]) <= int(L):
        return bool(True)
    if int(medidas[2]) <= int(H):
        return bool(True)
    if int(medidas[1]) <= int(H):
        return bool(True)
    if int(medidas[1]) <= int(L):
        return bool(True)
    if int(medidas[1]) > (H):
        return bool(False)
    if int(medidas[1]) > (L):
        return bool(False)
    if int(medidas[0]) > int(H):
        return bool(False)
    if int(medidas[0]) > int(L):
        return bool(False)
    if int(medidas[2]) > int(H):
        return bool(False)
    if int(medidas[2]) > int(L):
        return bool(False)