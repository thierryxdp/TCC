def qtd_divisores(num):
    cont=0
    for x in range(1,num+1):
        if num%x==0:
            cont+=1
    return