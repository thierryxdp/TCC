def soma_h(n):
    '''
    Funcao que recebe um numero inteiro. A funcao retorna a soma de termos de uma serie (1 + 1/2 + 1/3 + 1/4 + 1/5+...)
    int -> float
    ''' 
    soma = 0
    for i in range(1,n+1):
        termo = 1.0/(i)
        soma = soma + termo
    return round(soma,2)