def div_h(n):
    return 1/n
def soma_h(n):
    k=sum(list(map( div_h, range(n,0,-1))))
    return round(k,2)