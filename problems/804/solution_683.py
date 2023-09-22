def filtra_pares(a):
    """Dada uma tupla com 4 numeros inteiros essa funcao retorna os
    numeros pares dentro dessa tupla
    """
    x,y,z,w = a
    
    if int(a[0]%2==0) and int(a[1]%2==0) and int(a[2]%2==0) and int(a[3]%2==0):
        return a[0],a[1],a[2],a[3]
    elif int(a[0]%2==0) and int(a[1]%2==0) and int(a[2]%2==0):
        return a[0],a[1],a[2]
    elif int(a[0]%2==0) and int(a[1]%2==0) and int(a[3]%2==0):
        return a[0],a[1],a[3]
    elif int(a[0]%2==0) and int(a[2]%2==0) and int(a[3]%2==0):
        return a[0],a[2],a[3]
    elif int(a[1]%2==0) and int(a[2]%2==0) and int(a[3]%2==0):
        return a[1],a[2],a[3]
    elif int(a[0]%2==0) and int(a[1]%2==0):
        return a[0],a[1]
    elif int(a[0]%2==0) and int(a[2]%2==0):
        return a[0],a[2]
    elif int(a[0]%2==0) and int(a[3]%2==0):
        return a[0],a[3]
    elif int(a[1]%2==0) and int(a[2]%2==0):
        return a[1],a[2]
    elif int(a[1]%2==0) and int(a[3]%2==0):
        return a[1],a[3]
    elif int(a[2]%2==0) and int(a[3]%2==0):
        return a[2],a[3]
    elif int(a[0]%2==0):
        return a[0],
    elif int(a[1]%2==0):
        return a[1],
    elif int(a[2]%2==0):
        return a[2],
    elif int(a[3]%2==0):
        return a[3],
    else:
        return('()')