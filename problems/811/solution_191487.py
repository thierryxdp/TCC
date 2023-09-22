def colchao(medidas,H,L):
    var1 = 0
    var2 = 0
    if medidas[1] > H:
        var1 = var1 + 1
    if medidas[1] > L:
        var1 = var1 + 1
    if medidas[2] > H:
        var2 = var2 + 1
    if medidas[2] > L:
        var2 = var2 + 1
    else:
        return True
    if var1  + var2 <= 3:
        return True
    else:
        return False