def multiplo(x,n):
    if x%n==0:
        return x
def filtra_multipllos(lista,n):
    r=[]
    n=int
    for x in lista:
    if x%n==0:
        r=r+x
    return r