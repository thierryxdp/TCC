def filtra_pares(x):
    list1=[x]
    num=len(list1)
    par=[]
    for i in range (num):
        if (list1[i])%2==0:
            par.append(list1[i])
            
    return tuple(par)