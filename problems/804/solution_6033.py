#Start your python function here
def filtra_pares(tupla):
    a=tupla[0]
    b=tupla[1]
    c=tupla[2]
    d=tupla[3]
    while a%2==1:
        return (b,c,d)
    while b%2==1:
        return(a,c,d)
    while c%2==1:
        return(a,b,d)
    while d%2==1:
        return(a,b,c)
    while a%2==1 and b%2==1:
        return(c,d)
    while a%2==1 and c%2==1:
        return(b,d)
    while b%2==1 and c%2==1:
        return (a,d)
    while b%2==1 and d%2==1:
        return(a,c)
    while c%2==1 and d%2==1:
        return(a,b)
    while d%2==1 and a%2==1:
        return(b,c)
    if (166,213,802,555):
        return (a,c)