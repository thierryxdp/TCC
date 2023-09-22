def filtra_pares(a,b,c,d):
    numpar=[a,b,c,d]
    if numpar[0]%2==0:
        numpar=[0]
    elif numpar[1]%2==0:
            numpar=[1]
    elif numpar[2]%2==0:
            numpar=[2]
    elif numpar[3]%2==0:
            numpar=[3]
       return numpar