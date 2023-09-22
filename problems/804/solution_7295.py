def filtra_pares(numeros):
    (a,b,c,d)=numeros
    if ([a%2==0],[b%2==0],[c%2==0],[d%2==0]):
        return ([a,b,c,d])
    else:
        return ()