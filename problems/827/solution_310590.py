def qtd_divisores(num):
    primos=round((num+1)/2)
    contador=0
    for p in range(1,primos):
        if num%p==0:
            contador+=1
    return contador