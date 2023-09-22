def carros(pessoas,carros=6):
    """Essa função calcula a quantidade necessária de carros para transportar o numero total de pessoas para a viagem"""
    return (pessoas//carros)+(pessoas%carros)