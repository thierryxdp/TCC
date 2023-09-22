#int -> int
def qtd_divisores(num):
    #crio um contador pros divisores de num
    contador=1
    #calcula a quantidade de divisores de num
    if num<=0:
        return 0
    for p in range(1,num):
        if num==round((num/p))*p:
            contador+=1
    return contador