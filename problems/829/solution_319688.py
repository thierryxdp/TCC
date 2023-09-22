def soma_h(n):
    '''funcao que calcula e retorna o valor H com N termos
    int->float'''
    soma=0
    for n in range(1,n+1):
        soma = soma + 1/n
    return round(soma,2)