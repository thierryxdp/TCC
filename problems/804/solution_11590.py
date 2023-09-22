#Start your python function here
def filtra_pares(x):
    """
    Recebe uma tupla com quatro parametros e retorna uma nova tupla
    contendo apenas os elementos pares da tupla original
    na ordem em que aparecem;
    tupla -> tupla
    """
    if x[0]%2 == 0 and x[1]%2==0 and x[2]%2!=0 and x[3]%2!=0:
        return (x[0],x[1])
    elif x[0]%2 == 0 and x[2]%2==0 and x[3]%2!=0 and x[1]%2!=0:
        return (x[0],x[2])
    elif x[0]%2 == 0 and x[3]%2 == 0 and x[1]%2!=0 and x[2]%2!=0:
        return (x[0],x[3])
    elif x[1]%2 == 0 and x[2]%2 == 0 and x[3]%2!=0 and x[0]%2!=0:
        return (x[1],x[2])
    elif x[1]%2 == 0 and x[3]%2 == 0 and x[2]%2!=0 and x[0]%2!=0:
        return (x[1],x[3])
    elif x[2]%2 == 0 and x[3]%2 == 0 and x[0]%2!=0 and x[1]%2!=0:
        return (x[2],x[3])
    elif x[0]%2 == 0 and x[1]%2==0 and x[2]%2==0 and x[3]%2!=0:
        return (x[0],x[1],x[2])
    elif x[0]%2 == 0 and x[1]%2 == 0 and x[3]%2==0 and x[2]%2!=0:
        return (x[0],x[1],x[3])
    elif x[0]%2 == 0 and x[2]%2 == 0 and x[3]%2==0 and x[1]%2!=0:
        return (x[0],x[2],x[3])
    elif x[1]%2 == 0 and x[2]%2 == 0 and x[3]%2 == 0 and x[0]%2!=0:
        return (x[1],x[2],x[3])
    elif x[0]%2 == 0 and x[1]%2 == 0 and x[2]%2 == 0 and x[3]%2 == 0:
        return (x[0],x[1],x[2],x[3])
    elif x[3]%2==0 and x[2]%2!=0 and x[1]%2!=0 and x[0]%2!=0:
        return (x[3])
    elif x[0]%2==0 and x[1]%2!=0 and x[2]%2!=0 and x[3]%2!=0:
        return (x[0])
    elif x[1]%2==0 and x[2]%2!=0 and x[3]%2!=0 and x[0]%2!=0:
        return (x[1])
    elif x[2]%2==0 and x[3]%2!=0 and x[1]%2!=0 and x[0]%2!=0:
        return (x[2])
    else:
        return ()