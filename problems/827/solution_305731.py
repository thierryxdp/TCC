def qtd_divisores(num):
    '''Função que conta quantos divisores um número tem.
    num=int->int'''
    soma=0
    divisores=range(1,num+1)
    if num<0:
        return 0
    for y in w:
        if num%y==0:
            soma=soma+1
   	return divisores