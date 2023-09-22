def qtd_divisores(num):
    numero=0
    num=math.fabs(num)
    for i in range(1,int(num/2+1)):
        if num%i==0:
            numero+=1
    return numero+1