def soma_h(n):
    ''' Essa função calcula o valor de h;int->float'''
    i=0
    for numero in range(1,n+1):
        h=1/numero
        i+=h
    return round(i,2)