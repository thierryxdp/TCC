def repetidos(lis):
    """j"""
    i=0
    nlis=[]
    
    
    while (i<int(len(lis))):
        if int(lis[i])==int(lis[i-1]):
            nlis= nlis+[1]
            i=i+1
        else:
            i=i+1
    return len(nlis)