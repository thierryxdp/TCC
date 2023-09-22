def qtd_divisores(num):
    '''teste'''
    resultado=0
    for i in range(1,num+1):
        if num % i==0:
            resultado=resultado+1
    return resultado