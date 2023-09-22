#Start your python function here
def filtra_pares(a):
    
    if a[0] % 2 == 0:
        valor0 = a[0:1]
    else:
        valor0 = a[0:0]
    if a[1] % 2 == 0:
        valor1 = a[1:2]
    else:
        valor1 = a[1:1]
    if a[2] % 2 == 0:
        valor2 = a[2:3]
    else:
        valor2 = a[2:2]
    if a[3] % 2 == 0:
        valor3 = a[3:4]
    else:
        valor3 = a[3:3]
    return (valor0+valor1+valor2+valor3)