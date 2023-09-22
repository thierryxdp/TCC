def carros(pessoas,capacidade=5):
    if pessoas%capacidade >0:
        x=1
    else:
        x=0
    return pessoas//capacidade +x