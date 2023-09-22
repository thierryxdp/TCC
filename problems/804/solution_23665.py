def filtra_pares(x):
    Var=()
    Var1=int(x[0])
    Var2=int(x[1])
    Var3=int(x[2])
    Var4=int(x[3])
    if Var1%2==0:
        Var=Var+(Var1,)
    if Var2%2==0:
        Var=Var+(Var2,)
    if Var3%2==0:
        Var=Var+(Var3,)
    if Var4%2==0:
        Var=Var+(Var4,)
    return Var