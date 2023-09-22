#Start your python function here
def filtra_pares(a):
    if a[0] % 2 == 0:
        valor0 = a[0]
    else:
        valor0 = ''
    if a[1] % 2 == 0:
        valor1 = a[1]
    else:
        valor1 = ''
    if a[2] % 2 == 0:
        valor2 = a[2]
    else:
        valor2 = ''
    if a[3] % 2 == 0:
        valor3 = a[3]
    else:
        valor3 = ''

    return (valor0, valor1, valor2, valor3)