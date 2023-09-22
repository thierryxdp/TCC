def qtd_divisores(num):
    i=1
    while i in range(1,int(num)):
        if num%i==0:
        i=i+1
    return i