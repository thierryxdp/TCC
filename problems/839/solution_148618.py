def carros(pessoas,capacidade):
    """Função que calcula a quantidade de carros necessários para fazer a viagem 
       dado o número de pessoas e a capacidade dos carros."""
    if (pessoas/capacidade==int):
        return (pessoas/capacidade)
    else:
        return (pessoas//capacidade)+1