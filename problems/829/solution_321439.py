def soma_h(n):
    '''retorna a soma dos inversos de 1 ate n com 2 casas decimais;
    int->float'''
    resultado = 0
    for i in range(2,n+1):
        resultado = resultado + (1/i)
    return round(resultado,2)