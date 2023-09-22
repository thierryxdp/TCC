def qtd_divisores(num):
    '''Função que conta quantos divisores um número tem.
    num=int->int'''
    divisao=0
    w = range(1,num+1)
    if num<0:
        return 0
    for y in w:
        if num%y==0:
            divisao=divisa0+1
   	return divisao