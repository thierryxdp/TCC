def qtd_divisores(num):
    contador=1
    if num<=0:
        return 0
    for p in range(1,num):
        if num==round((num/p))*p:
            contador+=1
    return contador