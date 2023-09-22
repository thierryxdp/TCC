import math
def carros(np,cap=5):
    """Funcao calcular e retornar o número exato de carros necessários
    para esta viagem. Caso os veículos considerados sejam de 
    capacidades não convencionais, será dado também como entrada 
    a capacidade dos veículos, considerando que todos os veículos 
    são iguais"""
    if np==cap==0:
        return math.ceil(np/cap)
    else:
        a=math.ceil(np)
        b=math.ceil(cap)
        return (a//b)+1