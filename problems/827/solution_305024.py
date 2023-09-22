def qtd_divisores(num):
    '''teste'''
    resultado=1
    for i in range(2,num+1):
        if num % i==0:
            resultado=resultado+1
    return resultado