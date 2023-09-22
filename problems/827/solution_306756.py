def qtd_divisores(numero): 
    '''funçao que calcula quantos numeros sao divisíveis pelo número de entrada''' 
    '''int->int'''
    ndd=0
    for n in range(1,numero+1): 
        if numero%n==0: 
            ndd=ndd+1 
    return ndd