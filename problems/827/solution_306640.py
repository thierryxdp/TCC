def qtd_divisores(num):
    contador=0
    for n in range(1,num+1):
        if num%n==0:
            contador=contador+1
    return contador