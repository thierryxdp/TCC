def fracao(x):
    return 1/x
def soma_h(n):
    k=1
    l=0
    while k<=n:
        l+=fracao(k)
        k+=1
    return round(l,2)