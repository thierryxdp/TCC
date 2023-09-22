def carros(pessoas,capacidade=5):
    carros=pessoas/capacidade
    if pessoas%capacidade!=0:
        return carros+1
    else:
        return carros