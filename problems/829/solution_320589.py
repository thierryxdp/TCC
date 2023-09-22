def soma_h(n):
    x=1
    h=0
    while 1/x!=1/(n+1):
        h+=1/x
        x+=1
    return round(h,2)