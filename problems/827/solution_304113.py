import math
def qtd_divisores(num):
    """Para saber quantos divisores o número inteiro possui, digite;
    int-> lista"""
    numero=0
    if num<0:
        return 0
    for i in range(1,int(num/2+1)):
        if num%i==0:
            numero+=1
    return numero+1