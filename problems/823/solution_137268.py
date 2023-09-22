def faltante(N):
    numerodetermos=len(N)+1
    y=N[0:1]+N[-1:]
    soma=sum(y)
    total=(soma*numerodetermos)//2
    total2=sum(N)
    re=total-total2
    if re not in N:
        return re
    else:
        return sum(N[-1:])+1