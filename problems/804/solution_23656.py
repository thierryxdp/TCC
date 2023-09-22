def e_par(x):
    if x%2==0:
        return x
    else:
        return " "
def filtra_pares(a):
    return e_par(a[0]), e_par(a[1]), e_par(a[2]), e_par(a[3])