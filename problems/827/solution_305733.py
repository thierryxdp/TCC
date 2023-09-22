def qtd_divisores(num):
    '''Função que conta quantos divisores um número
    tem.
    n=int->int'''
    divi=0
    quant=range(1,num+1)
    if num<0:
        return 0
    for y in quant:
        if num%y==0:
            divi=divi+1
    return divi