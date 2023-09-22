def soma_h(N):
    '''Função que calcula e retorna o valor de H com N termos; int -> float'''
    soma=0
    for i in list(range(1,N+1)):
        soma=soma+(1/i)
    return round(soma,2)