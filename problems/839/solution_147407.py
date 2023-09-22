from math import ceil  
def carros(p,cp=5):
    """Função que calcula o número de carros necessários para realizar uma viagem dado o número de pessoas p e a capacidade de cada carro cp, se a última não for fornececida a capacidade considerada será de 5 pessoas;int,int->int"""
return ceil(p/cp)