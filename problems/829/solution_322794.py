def soma_h(N):
    ''' Função que calcula e retorna o valor de h (h= 1+1/2+1/3+...+1/N) com n termos,onde N é inteiro
    e é dado como entrada; int->float'''
    soma=0
    for i in range(1,N+1):
        soma+= 1/i
    return round(soma,2)