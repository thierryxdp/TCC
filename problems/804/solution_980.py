#Start your python function here
def filtra_pares(w,x,y,z):
    """ Para fazer a filtragem de numeros pares, digite;
    int,int,int,int->int"""
    if (w)%2 == 0:
        return w
    elif (x)%2 == 0:
        return x
    elif (y)%2 == 0:
        return y
    elif (z)%2 == 0:
        return z
    elif (w)%2 and (x)%2== 0 and (y)%2== 0 and (z)%2== 0:
        return w,x,y,z