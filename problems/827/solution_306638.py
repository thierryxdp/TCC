def qtd_divisores(num):
    contador=0
    for n in range(num):
        if num%n==0:
            contador=contador+1
    return contador