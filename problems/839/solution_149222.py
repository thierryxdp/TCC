def carros (numpessoas,capacidade=5):
    """Essa função recebe o número de pessoas e capacidade de um veículo
    e calcula quantos veículos são necessários para comportar todas as
    pessoas. Caso a capacidade não seja a convencional de 5 pessoas,a capa-
    cidade deve ser informada. int,int"""
    carros = numpessoas//capacidade
    return carros