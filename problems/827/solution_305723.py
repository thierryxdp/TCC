def qtd_divisores(num):
    '''Função que conta quantos divisores um número tem.
    num=int->int'''
    divis=0
    w = range(1,num+1)
    if num<0:
        return 0
    for y in w:
        if num%y==0:
            divis=divis+1
   	return divis