def carros(pessoas,capacidade=5):
    """Função que calcula o número de veículos necessários para fazer a viajem 
       dados os números de pessoas e a capacidade de cada veículo."""
    if (pessoas/capacidade)==int:
        return (pessoas//capacidade)+1
    else:
        return pessoas/capacidade