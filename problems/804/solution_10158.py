def filtra_pares(x,y,w,z):
    '''funcao que retorna quais sao os numeros pares da tupla
    de entrada
    (int,int,int,int) -> (int,int,int,int)'''
    filtra_x=x%2
    filtra_y=y%2
    filtra_w=w%2
    filtra_z=z%2
    if filtra_x==0 and filtra_y==0 and filtra_w==0 and filtra_z==0:
        return (x,y,w,z)
    elif filtra_x==0 and filtra_y==0 and filtra_w==0 and not filtra_z==0:
        return (x,y,w)
    elif filtra_x==0 and filtra_y==0 and not filtra_w==0 and filtra_z==0:
        return (x,y,z)
    elif filtra_x==0 and not filtra_y==0 and filtra_w==0 and filtra_z==0:
        return (x,w,z)
    elif not filtra_x==0 and filtra_y==0 and filtra_w==0 and filtra_z==0:
        return (y,w,z)
    elif filtra_x==0 and filtra_y==0 and not filtra_w==0 and not filtra_z==0:
        return (x,y)
    elif filtra_x==0 and not filtra_y==0 and filtra_w==0 and not filtra_z==0:
        return (x,w)
    elif filtra_x==0 and not filtra_y==0 and not filtra_w==o and filtra_z==0:
        return (x,z)
    elif not filtra_x==0 and filtra_y==0 and filtra_w==0 and not filtra_z==0:
        return (y,w)
    elif not filtra_x==0 and filtra_y==0 and not filtra_w==0 and filtra_z==0:
        return (y,z)
    elif not filtra_x==0 and not filtra_y==0 and filtra_w==0 and filtra_z==0:
        return (w,z)
    elif filtra_x==0 and not filtra_y==0 and not filtra_w==0 and not filtra_z==0:
        return (x)
    elif not filtra_x==0 and filtra_y==0 and not filtra_w==0 and not filtra_z==0:
        return (y)
    elif not filtra_x==0 and not filtra_y==0 and filtra_w==0 and not filtra_z==0:
        return (w)
    elif not filtra_x==0 and not filtra_y==0 and not filtra_w==0 and filtra_z==0:
        return (z)
    else:
        return ()