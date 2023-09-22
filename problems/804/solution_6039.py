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