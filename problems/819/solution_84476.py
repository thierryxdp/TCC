def filtraMultiplos(lista,n):
    if lista[0]%n==0:
        return [lista[0]]
    elif lista[1]%n==0:
        return [lista[1]]
    elif lista[2]%n==0:
        return lista[2]
    elif lista[3]%n==0:
        return lista[3]
    elif lista[4]%n==0:
        return lista[4]
    elif lista[5]%n==0:
        return lista[5]
    elif lista[6]%n==0:
        return lista[6]
    else:
        return []