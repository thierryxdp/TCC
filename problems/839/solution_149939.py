def carros_aprox(pessoas,capacidade=5):
    """Retorna o numero aproximado de carros necessarios para realizar uma viagem, dado o numero de pessoas e o a capacidade de carros, que caso nao informada sera considerado o valor padrao de 5"""
    return 1 + (pessoas/capacidade)

def carros(pessoas,capacidade=5):
    """Retorna o numero aproximado de carros necessarios para realizar uma viagem, dado o numero de pessoas e o a capacidade de carros, que caso nao informada sera considerado o valor padrao"""
return round carros