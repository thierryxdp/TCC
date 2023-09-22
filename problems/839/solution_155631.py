def carros(np,cap=5):
    """ Função para calcular e retornar o número exato de carros,
    considerando que seja dado como entrada o número de pessoas.
    Caso os veículos considerados sejam de capacidades,5, será
    dado também como entrada a capacidade dos veículos,
    considerando que todos os veículos são iguais"""
    if cap<5:
        return np
    elif cap==np:
        return np//cap
    else:
        return 1+(np//cap)