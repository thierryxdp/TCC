def qtd_divisores(num):
    '''recebo um numero inteiro e retorno quantos divisores este numero possui.
int->int'''
    contador=0
    for x in range(1,num+1):
        if num % x==0:
            contador += 1
    return contador