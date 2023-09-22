def maiores(l,n):
    listaf=[]
    x=0
    while x<len(l):
        if l[x]>n:
            listaf += [(listaf),]
        x=x+1
    return listaf