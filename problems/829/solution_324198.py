def fracao(x):
    return 1/x
def soma_h(n):
    k=0
    while k<=n:
        k+=fracao(k)
        k+=1
    return round(k,2)