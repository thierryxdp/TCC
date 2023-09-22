def maiores(l,n):
    list.append(l,n)
    list.sort(l)
    x=str(l)
    s1=str.replace(x,'[','')
    s2=str.replace(s1,',','')
    s3=str.replace(s2,']','')
    y=str(n)
    l2=s3[str.index(s3,y):]
    l3=l2[str.count(l2,y)+str.count(l2,y):]
    l4=list(l3)
    list.remove(l4,list.pop(l4,1))
    return l4