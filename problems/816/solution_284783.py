def maiores(lis,n):
    f=[0]
    i=0
    while i<len(lis):
        if(lis[i]>n):
            f.append(lis[i])
        i=i+1
    return f