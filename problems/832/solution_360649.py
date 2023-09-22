def eh_quadrada(M):
    i=1
    x=1
    while i<len(M):
        if len(M[i])==len(M[i-1]):
            x=x*1
        i=i+1
        if len(M[i])!=len(M[i-1]):
            x=x*0
        i=i+1
    if x==0:
        return False
    else:
        return True