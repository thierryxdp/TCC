def fatorial(numero):
    '''dado um número, calcula o fatorial deste número;
    int --> int'''
    num=numero
    fatorial=1
    if num>0:
        while num>0:
            fatorial=fatorial*num
            num=num-1
        return fatorial
    elif num==0:
        return 1
    elif num<0:
        return 'nao existe'