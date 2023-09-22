def carros(pessoas, capacidade = 5):
    '''
    Ambos os valores devem ser números inteiros
    Quantidade de carros é dada por: quantidade de pessoas dividida
    pela capacidade do carro, que o padrão é 5
    	caso a divisão tenha resto, math.ceil arrendodará o valor para cima,
    e o último carro levará uma quantidade menor de pessoas do que sua capaci-
    dade máxima.
    '''
    quantidade = math.ceil(pessoas / capacidade)
    return quantidade