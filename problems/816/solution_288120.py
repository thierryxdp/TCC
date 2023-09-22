def maiores(l,n):
    listaf=[]
    x=0
    while x<len(l):
        if l[x]>n:
            listaf+=[l[x],]
        x=x=1
    list.sort(listaf)
    return listaf