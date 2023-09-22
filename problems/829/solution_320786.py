def soma_h(N):
    '''Funçao para calcular e retornar o valor H com N termos 
    onde N é inteirp e dado como entrada'''
    soma = 0
    for i in range (1,N+1):
        soma += 1.0/i
        return round(soma,2)