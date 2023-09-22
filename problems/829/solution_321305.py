def soma_h(n):
    '''Calcula e retorna o valor de H que é a soma de 1 sobre n termos.
    int-->float'''
    valor=0
    for i in range(1,n+1):
        valor=valor+(1/i)
    return round(valor,2)