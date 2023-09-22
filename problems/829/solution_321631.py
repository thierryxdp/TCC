def soma_h(n):
    ''' Função para calcular e retornar o valor H com N termos da formula dada
    int->float'''
    soma=0
    for i in range(1, n+1):
        
        soma = soma + (1/i)

    return soma