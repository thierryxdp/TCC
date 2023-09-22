def qtd_divisores(num):
    quantidade=1
    if num<0:
        return 0
    for i in range(1,num):
        if num%i==0:
            quantidade+=1
    return quantidade