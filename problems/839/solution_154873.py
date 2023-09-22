def carros(capacidade, pessoas = 5):
    tipo = type(capacidade/pessoas)
    if type(capacidade/pessoas) == float:
        return(int(capacidade/pessoas)+1)
    else:
        return int(capacidade/pessoas)
    
def carros(capacidade1, pessoas1=5):
    """calcula a quantidade carros para a viagem"""
    return int(capacidade1/pessoas1)