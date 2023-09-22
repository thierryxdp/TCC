def soma_h(n):
    '''Essa função tem como objetivo somar um valor por 'n' vezes para
    saber o retorno de H.'''
    '''int -> int'''
    soma = 0
    for i in range (1,n+1):
        soma = soma + (1/i)
        
    return round(soma,2)