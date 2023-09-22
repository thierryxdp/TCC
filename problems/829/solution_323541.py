def soma_h(n):
    '''Essa função tem como objetivo somar um valor por 'n' vezes para
    saber o retorno de H.'''
    '''int -> int'''
    i = 0
    n = 1
    soma = 0
    while i < n:
        soma += (1/n)
        i+=1
        n+=1
    return soma