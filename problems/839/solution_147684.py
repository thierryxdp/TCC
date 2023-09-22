def carros(pessoas, capacidade): 
    if pessoas % capacidade  == 0:
        return pessoas//capacidade
    else:
        return (pessoas//capacidade) + 1