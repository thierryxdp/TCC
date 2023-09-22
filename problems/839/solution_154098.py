def carros(p:int,c:int = 5) -> int:
    "N° de carros, dados a quantidade de pessoas e a capacidade do veículo se não convencional."
    carros = p/c
    return math.ceil(carros)