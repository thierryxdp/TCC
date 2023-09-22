def soma_h(n):
    ''' Função que define a "soma fatorial inversa" de um dado número n
    int -> float '''
    soma = 0
    for x in list(range(n+1)):
        if x > 0:
        	soma = soma + (1/x)
    return round(soma, 2)