def soma_h(N):
    '''Recebe um numero inteiro N e Retorna o valor de H baseado na 
    formula ao lado;
    int -> float'''
    x=list(range(1,N+1))
    soma=0
    for i in x:
        soma = soma + (1/i)
    return round(soma, 2)