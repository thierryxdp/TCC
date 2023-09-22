def filtra_pares(a):
    """Retorna uma tupla somente com os elementos pares da tupla que é o parâmetro;
    tup->tup"""
    if a[0]%2=0 and a[1]%2=0 and a[2]%2=0 and a[3]%2=0:
        return a
    elif a[0]%2=0 and a[1]%2=0 and a[2]%2=0 and a[3]%2=1:
        return a[0:3]
    elif a[0]%2=0 and a[1]%2=0 and a[2]%2=1 and a[3]%2=0:
        return a[0:2]+a[3:]
    elif a[0]%2=0 and a[1]%2=1 and a[2]%2=0 and a[3]%2=0:
        return a[0:1]+a[2:]
    elif a[0]%2=1 and a[1]%2=0 and a[2]%2=0 and a[3]%2=0:
        return a[1:]
    elif a[0]%2=0 and a[1]%2=0 and a[2]%2=1 and a[3]%2=1:
        return a[0:2]
    elif a[0]%2=0 and a[1]%2=1 and a[2]%2=0 and a[3]%2=1:
        return a[1:2]+a[3:]
    elif a[0]%2=1 and a[1]%2=0 and a[2]%2=0 and a[3]%2=1:
        return a[1:3]
    elif a[0]%2=0 and a[1]%2=1 and a[2]%2=1 and a[3]%2=0:
        return a[0:1]+a[3:]
    elif a[0]%2=1 and a[1]%2=0 and a[2]%2=1 and a[3]%2=0:
        return a[1:2]+a[3:]
    elif a[0]%2=1 and a[1]%2=1 and a[2]%2=0 and a[3]%2=0:
        return a[2:]
    elif a[0]%2=0 and a[1]%2=1 and a[2]%2=1 and a[3]%2=1:
        return a[0:1]
    elif a[0]%2=1 and a[1]%2=0 and a[2]%2=1 and a[3]%2=1:
        return a[1:2]
    elif a[0]%2=1 and a[1]%2=1 and a[2]%2=0 and a[3]%2=1:
        return a[2:3]
    elif a[0]%2=1 and a[1]%2=1 and a[2]%2=1 and a[3]%2=0:
        return a[3:]
    else:
        return ()