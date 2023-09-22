def carros(pessoas, capacidade=5):
    '''calcula o numero de carros necessarios para uma viagem dado o numero de pessoas e se preciso a capacidade do veiculo
    int, int => float'''
    carros = pessoas/capacidade
    return math.ceil(carros)