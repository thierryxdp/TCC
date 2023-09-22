def carros(p,c):
    """divide o número de pessoas p pela capacidade de cada carro c e arredonda o resultado "pra cima" retornando o número de carros necessários
    int,int->int"""
    import math 
    return ceil(p/c)