def qtd_divisores(num):
    quantidade=1
    i=1
    for i in range(num):
        if num%i==0:
            quantidade+=1
    return quantidade