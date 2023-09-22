def fatorial (num):
    '''retorna o fatorial de um int num
    int->int'''
    num3=num
    num2=num
    while num2>0:
        num2=num2-1
        num3=num3*num2
    return num3