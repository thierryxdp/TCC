def soma_h(n):
    '''Funcao que recebe um numero e retorna o valor H com N termos, sendo o
parametro'''
    soma = 0
    for i in range(1,n+1):
        soma += 1.0/i
    return round(soma,2)