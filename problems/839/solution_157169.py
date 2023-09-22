import math
def carros(num_pessoas,capacidade_carro=5):
    
    """função que ira calcular o numero de carros necessarios
    para transportar um determinado numero de pessoas
    int,int = int
    """
    
    carro= num_pessoas / capacidade_carro
    
    return int(carro+ 0.5)