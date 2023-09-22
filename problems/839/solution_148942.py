def carros(pessoas, capacidade = 5):
    'Retorna a quantidade de carros, dividindo a capacidade dos carros pelo número de pessoas'
    return math.ceil(pessoas/capacidade)