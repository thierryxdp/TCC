import math
def carros(pessoas, capacidade=5):
    """ documentação do número de carros necessários 
    para uma viagem em grupo """
    return  math.ceil(pessoas // capacidade)