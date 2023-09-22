def soma_h(n):
    '''Calcula e retorna o valor H com N termos onde N é inteiro e dado com entrada.
    int->float
    '''
    h=0
    for x in range(1,n+1):
         h=h+(1/x)
    return round(h,2)