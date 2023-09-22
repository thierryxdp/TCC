def carros(pessoas,carro5=5,carro6=6,carro4=4):
    """Essa função calcula a quantidade necessária de carros para transportar o numero total de pessoas para a viagem"""
    return (pessoas//carro5)+(pessoas%carro5)