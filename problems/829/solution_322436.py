def soma_h(n):
    '''retorna a soma das inversas de n numeros;
    int->float'''
    h=0
    for numero in range(1,n+1):
        h=h+numero**-1
    return round(h,2)