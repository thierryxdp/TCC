def carros(pessoas,capacidade = 5):
    "Essa função calcula a quant de carros necessarias para conter todas as pessoas informadadas"
    carros = (pessoas//capacidade)+1
    return carros