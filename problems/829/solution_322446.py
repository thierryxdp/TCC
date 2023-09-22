def soma_h(N):
    '''Funcao que calcula e retorna o valor de H com N termos, onde N é dado como parametro. Retorne o resultado somente com 2 casas decimais'''
    '''int -> float'''
    soma = 0
    
    for x in range(1,N+1):
        soma = soma + 1/x
    return round(soma,2)