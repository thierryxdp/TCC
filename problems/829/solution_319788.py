def soma_h(N):
    '''Função que calcula e retorna o valor de H com N termos; int -> float'''
    soma=0
    for i in list(range(1,N+1)):
        numero= 1/N
        soma=soma+numero
    return round(soma,2)