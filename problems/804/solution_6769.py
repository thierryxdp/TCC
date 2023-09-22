def filtra_pares(x):
    if x[0]%2==0:
        nova_x0=x[0]
    elif x[0]%2!=0:
        x=x[1:]
    if x[1]%2==0:
        nova_x1=x[1]
    if x[2]%2==0:
        nova_x2=x[2]
    if x[3]%2==0:
        nova_x3=x[3]
    return (nova_x0,nova_x1,nova_x2,nova_x3)