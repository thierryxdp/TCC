def qtd_divisores(num):
    ''' retorna o numero de divisores que o numero tem,int->int'''
    i=0
    for numero in range(1,num+1):
        if num%numero==0:
            i=i+1
    return i