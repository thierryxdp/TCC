def eh_quadrada(m):
    l=0
    for i in range(len(m)):
        b=len(m[i])
        if(b!=len(m)):
            l=l+1
    if(l==0):
        return True
    elif(l!=0):
        return False