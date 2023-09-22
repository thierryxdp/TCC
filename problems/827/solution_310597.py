def qtd_divisores(num):
    contador=2
    if num<=0:
        return 0
    for p in range(1,num):
        if num%p==0:
            contador+=1
    return contador