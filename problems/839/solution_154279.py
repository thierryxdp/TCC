import math 

def carros(n_pessoas, capacidade = 5):
    """Calcular ...
    
    Assume-se pelo menos 1 pessoa.
    int -> int
    
    Casos de teste:
    carros(1) == 1
	carros(5) == 1
    carros(6) == 2
    """
    return math.ceil(n_pessoas/capacidade)