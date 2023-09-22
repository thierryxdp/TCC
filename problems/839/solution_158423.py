def carros(pessoas,capacidade = 5):
    "Essa função calcula a quant de carros necessarias para conter todas as pessoas informadadas"
    carros = math.ceil(pessoas/capacidade)
    return carros