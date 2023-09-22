def filtra_pares(elem):
    list=()
    if elem[0] &2 ==0:
        list = list +(elem[0],)
    if elem[1] %2==0:
        list= list+(elem[1],)
    if elem[2]%2==0:
        list= list +(elem[2],)
    if elem[3]%2==0:
        list= list + (elem[3],)
    return list