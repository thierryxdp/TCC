def soma_h(numero):
    '''funçao que calcula e retorna o valor de H com N termos;
     int->float'''
    soma=0
    for N in range(1,numero+1):
        soma= soma + 1/N
    return round(soma,2)