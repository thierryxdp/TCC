def qtd_divisores(num):
    i=0
    for numero in range(1,num+1):
        if num%numero==0:
            i=i+1
    return i