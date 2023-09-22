def carros(p,c=5):
    '''calcula e retorna o número de carros necessário para transportar um grupo de pessoas(p: número de pessoas, c=capacidade do veículo)'''
    return math.ceil(p/c)