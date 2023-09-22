def qtd_divisores(num):
    '''retorna q quantidade de divisores de um numero
    int->int'''
    t=0
    for i in range(1,num+1):
        if num%i == 0:
            t+=1
    return t