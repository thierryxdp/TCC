def fatorial(n):
    '''dado um numero, a função retorna o fatoria
   	int->int'''
    
    num = 1
    while n >= 1:
        num=num-n
        n= n-1
    return num