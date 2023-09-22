def filtra_pares(x):
    
    var = ()
    var1 = int(x[0])
    var2 = int(x[1])
    var3 = int(x[2])
    var4 = int(x[3])
    if var1%2 == 0:
        var= var + (var1,)
    if var2%2 == 0:
        var= var+ (var2,)
    if var3%2 == 0:
        var= var+ (var3,)
    if var4%2 == 0:
        var= var+ (var4,)
    return var