def carros(pessoas,capacidade=5):
    carro=(pessoas/capacidade) + (pessoas % capacidade>0)
    return (carro)