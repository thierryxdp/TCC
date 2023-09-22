def fracao(x):
    return 1/x
def soma(n):
    k=1
    while k<=n:
        k+=fracao(k)
        k+=1
    return round(k,2)