def fatorial(num):
    '''retorna a fatorial de um numero;
    int->int'''
    while num>0:
        result=num
        resultado=result*num-1
        num=num-1
    return resultado