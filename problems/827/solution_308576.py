def qtd_divisores(num):
    a=0
    i=1
    for i in range(num):
        if num%i==0:
            a+=1
    return a