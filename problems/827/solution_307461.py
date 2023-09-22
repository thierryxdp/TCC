def qtd_divisores(n):
    nn=[2,3,5,7,11]
    r=0
    for i in nn:
        if n%i==0:
            r+=1
    return r