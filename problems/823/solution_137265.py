def teste(N):
    numerodetermos=len(N)+1
    y=N[0:1]+N[-1:]
    soma=sum(y)
    total=(soma*numerodetermos)//2
    total2=sum(N)
    return total-total2