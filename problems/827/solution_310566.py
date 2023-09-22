def qtd_divisores(num):
    cont=0
    for x in range(1,num):
        if num%x==0:
            cont+=1
    return