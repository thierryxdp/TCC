def carros(pessoas,capacidade=5):
    """Função que calcula o número de veículos necessários para fazer a viajem 
       dados os números de pessoas e a capacidade de cada veículo."""
    if (pessoas%capacidade<1) and (pessoas%capacidade>0):
        return (pessoas//capacidade)+1
    else:
        return pessoas/capacidade