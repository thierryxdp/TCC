def qtd_divisores(num):
    cont=0
    for i in range(2,int(num/2+1)):
        if num%i==0:
            cont+=1
    return num