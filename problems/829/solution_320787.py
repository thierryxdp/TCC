def soma_h(n):
    '''Funçao para calcular e retornar o valor H com N termos 
    onde N é inteirp e dado como entrada'''
    soma = 0
    for i in range(1,n+1):
        soma = soma + 1/i
    return round(soma,2)