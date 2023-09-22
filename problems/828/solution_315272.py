def primos(n):
    soma=0
    for x in range(2,n):
        if n%x==0:
            soma=soma+1
    if soma==0:
        return True
    else:
        return False