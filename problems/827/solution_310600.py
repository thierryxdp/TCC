def qtd_divisores(num):
    contador=0
    if num<=0:
        return 0
    for p in range(1,num):
        if num==(num/p)*p:
            contador+=1
    return contador