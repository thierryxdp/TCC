def qtd_divisores(num):
    '''função que calcula quantos o numero de divisores de um numero'''
    cont = 0
    for i in range(1,num+1):
        if num % i==0:
            cont+=1
    return cont