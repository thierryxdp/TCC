def filtra_pares(n1,n2,n3,n4):
    list1=[n1,n2,n3,n4]
    num=len(list1)
    par=[]
    for i in range (num):
        if (list1[i])%2==0:
            par.append(list1[i])
            
    return tuple(par)