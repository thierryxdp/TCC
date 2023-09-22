def soma_h(n):
    i=1
    s=0
    while i <n:
        s+=(1/(1+i))
        i+=1
    return round(1+s,2)