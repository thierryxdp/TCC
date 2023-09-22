def carros(pessoas,capacidade=5):
    '''calcula o valor exato de carros necessários para uma viagem dado
    um número de passageiros
    int,int->int'''
    return math.ceil(pessoas/capacidade)