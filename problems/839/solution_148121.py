def carros(p,c=5):
    """dado o número de pessoas p e a capacidade de pessoas por carro c, calcula quantos carros serão necessários para realizar a viagem"""
    if p%c==0:
        return p/c
    else:
        return p//c+1