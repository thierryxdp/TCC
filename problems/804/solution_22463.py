def filtra_pares(s):
    
    var = ()
    var1 = int(s[0])
    var2 = int(s[1])
    var3 = int(s[2])
    var4 = int(s[3])
    
    if var1%2 == 0:
        var= var + (var1,)
    
    if var2%2 == 0:
        var= var+ (var2,)
    
    if var3%2 == 0:
        var= var+ (var3,)
    
    if var4%2 == 0:
        var= var+(var4)
    return var