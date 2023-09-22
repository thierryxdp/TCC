def carros(pessoas,capacidade):
    "Retorna exatamente quantos carros serão necessários para a viagem dado a quantidade de pessoas e a capacidade do veículo"
    return math.ceil(pessoas/capacidade)