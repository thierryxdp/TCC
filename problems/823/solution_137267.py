def faltante(N):
    numerodetermos=len(N)+1
    y=N[-1:]
    soma=sum(y)+1
    total=(soma*numerodetermos)//2
    total2=sum(N)
    return total-total2