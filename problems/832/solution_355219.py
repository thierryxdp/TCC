def eh_quadrada(m):
    a=len(m)
    b=len(m[0])
    if a==b:
        return True
    elif (a==1 and b==0):
        return True
    else:
        return False