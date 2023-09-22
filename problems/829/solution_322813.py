def soma_h(n):
    h=0
    for num in (range(1,n+1)):
        h = h + 1/num
    return round(h,2)