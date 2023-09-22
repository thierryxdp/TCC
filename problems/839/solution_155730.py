import math
def carros(pessoas,capacidade=5):
    """Função que retorna a quantidade exata de carros, dada uma quantidade de pessoas a serem transportadas. Caso os veículos considerado sejam de capacidades não convencionais,
    será dado também como entrada a capacidade dos veículos."""
    return math.ceil(pessoas/capacidade)