def filtra_pares(x):
    '''Dada uma tupla x de quatro números inteiros, retorna uma tupla com os números pares de x; tupla->tupla'''
    if x[0]%2==0 and  x[1]%2!=0 and x[2]%2!=0 and x[3]%2!=0:
        lista2=x[0]
        return lista2
    if x[0]%2!=0 and  x[1]%2==0 and x[2]%2!=0 and x[3]%2!=0:
        lista2=x[1]
        return lista2
    if x[0]%2!=0 and  x[1]%2!=0 and x[2]%2==0 and x[3]%2!=0:
        lista2=x[2]
        return lista2
    if x[0]%2!=0 and  x[1]%2!=0 and x[2]%2!=0 and x[3]%2==0:
        lista2=x[3]
        return lista2
    if x[0]%2==0 and  x[1]%2==0 and x[2]%2!=0 and x[3]%2!=0:
        lista2=x[0],x[1]
        return lista2
    if x[0]%2==0 and  x[1]%2!=0 and x[2]%2==0 and x[3]%2!=0:
        lista2=x[0],x[2]
        return lista2
    if x[0]%2==0 and  x[1]%2!=0 and x[2]%2!=0 and x[3]%2==0:
        lista2=x[0],x[3]
        return lista2
    if x[0]%2!=0 and  x[1]%2==0 and x[2]%2==0 and x[3]%2!=0:
        lista2=x[1],x[2]
        return lista2
    if x[0]%2!=0 and  x[1]%2==0 and x[2]%2!=0 and x[3]%2==0:
        lista2=x[1],x[3]
        return lista2
    if x[0]%2!=0 and  x[1]%2!=0 and x[2]%2==0 and x[3]%2==0:
        lista2=x[2],x[3]
        return lista2
    if x[0]%2==0 and  x[1]%2==0 and x[2]%2==0 and x[3]%2!=0:
        lista2=x[0],x[1],x[2]
        return lista2
    if x[0]%2==0 and  x[1]%2==0 and x[2]%2!=0 and x[3]%2==0:
        lista2=x[0],x[1],x[3]
        return lista2
    if x[0]%2==0 and  x[1]%2!=0 and x[2]%2==0 and x[3]%2==0:
        lista2=x[0],x[2],x[3]
        return lista2
    if x[0]%2!=0 and  x[1]%2==0 and x[2]%2==0 and x[3]%2==0:
        lista2=x[1],x[2],x[3]
        return lista2
    if x[0]%2!=0 and  x[1]%2!=0 and x[2]%2!=0 and x[3]%2!=0:
        lista2=
        return lista2
    else:
        lista2=x[0],x[1],x[2],x[3]
        return lista2