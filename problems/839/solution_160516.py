def carros(pessoas,capacidade):
    '''calcula a quantidade de carros de diferentes capacidades necessarios para transportar um numero de pessoas'''
    return max(pessoas//capacidade)