def repetidos(lis):
    """j"""
    i=0
    nlis=[]
    a=int(lis[i])
    b=int(lis[i-1])
    
    while (i<int(len(lis))):
        if a==b:
            nlis= nlis+[1]
            i=i+1
        else:
            i=i+1
    return len(nlis)