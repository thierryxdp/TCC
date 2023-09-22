def soma_h(n):
    h=0
    for i in list(range(1,n+1)):
        h=h+1/i
    return round(h,2)