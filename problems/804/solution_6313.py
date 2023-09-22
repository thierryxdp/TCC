def filtra_pares(x):
    '''teste'''

    resultado=()

    n1=int(x[0])
    n2=int(x[1])
    n3=int(x[2])
    n4=int(x[3])

    if n1%2==0:
        resultado=resultado+n1
        
    if n2%2==0:
        resultado=resultado+n2

    if n3%2==0:
        resultado=resultado+n3

    if n4%2==0:
        resultado= resultado+n4

    return resultado