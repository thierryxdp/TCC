def filtra_pares(x):
    """filtra os elementos pares de uma tupla de 4 elementos"""
    var1 = int(x[0])
    var2 = int(x[1])
    var3 = int(x[2])
    var4 = int(x[3])
    var5 = ()
    if var1%2 == 0:
        var5 = var5 + (var1,)
    if var2%2 == 0:
        var5 = var5 + (var2,)
    if var3%2 == 0:
        var5 = var5 + (var3,)
    if var4%2 == 0:
        var5 = var5 + (var4,)
    return var5