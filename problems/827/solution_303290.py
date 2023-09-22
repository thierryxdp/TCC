def qtd_divisores(n):
    '''retorna quantos divisores tem um numero n
    int->int'''
    divi=0
    for i in range(1,n+1):
        if n%i==0:
            divi+=1
    return divi