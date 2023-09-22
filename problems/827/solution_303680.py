def qtd_divisores(num):
    for i in range(1,int(num)):
        if num%i==0:
            return i
    return i