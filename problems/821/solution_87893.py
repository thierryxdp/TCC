def fatorial(num):
    '''retorna a fatorial de um numero;
    int->int'''
    result=num
    while num>0:
        result=result*num-1
        num=num-1
    return result