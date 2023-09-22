def div(numero):
    d=[]
    for n in range(1, numero+1):
        if numero%n==0:
            d.append(n)
    return len(d)