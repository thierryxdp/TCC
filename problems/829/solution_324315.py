def soma_h(n):
    '''
    Calcula e retorna o valor H para N termos de entrada
    Retorna a soma com duas casas decimais
    '''
    h = 0
    for i in range(1,n+1):
        h = h + 1/i
    return round(h,2)