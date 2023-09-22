def carros (x:float, y = 5) -> float:
    '''Calcula a quantidade de carros necessários para fazer uma viagem com x passageiros e , se não convencionais, a capacidade dos carros usados (assume-se que todos possuem a mesma capacidade)'''
    return math.ceil(x/y)