def filtra_pares(A,B,C,D):
    pares=[]
    inteiros=(A,B,C,D)
    if inteiros[0]%2==0:
        list.insert(pares,0,inteiros[0])
    if inteiros[1]%2==0:
        list.insert(pares,1,inteiros[1])
    if inteiros[2]%2==0:
        list.insert(pares,2,intieros[2])
    if inteiros[3]%2==0:
        list.insert(pares,3,inteiros[3])
    return pares

#Start your python function here