def qtd_divisores(n):
    """k"""
    i=0
    lis=[]
    while i<n:
        if n%i ==0:
            lis=lis+i
            i=i+1
        else:
            i=i+1
    return lis