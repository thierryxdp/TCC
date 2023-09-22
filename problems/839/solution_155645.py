def carros(np,cap=5):
    """Funcao que retorna o numero de carros necessarios
    para fazer a viagem, considerando o numeros de pessoas,
    e a capacidade, senao informada, sera 5"""
    if np==cap:
        if (cap or np)==0:
            return 0
        else:
            return 1
    else:
        return 1+(np//cap)