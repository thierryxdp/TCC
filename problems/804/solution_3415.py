def filtra_pares(t2):
    pares =[0,1,2,3]
    if t2[0]%2==0 and t2[1]%2==0 and t2[2]%2==0 and t2[3]%2==0:
        return t2[0] , t2[1] , t2[2], t2[3]
    elif t2[0]%2!=0:
        return  t2[1] , t2[2],t2[3]
    if t2[0]%2==0 and t2[1]%2==0 and t2[2]%2==0:
        return t2[0] , t2[1] , t2[2]
    if t2[0]%2==0 and  t2[2]%2==0:
        return t2[0] ,  t2[2]
    if t2[0]%2==0 and t2[1]%2==0:
        return t2[0] ,  t2[1]
    if t2[0]%2==0:
        return t2[0]