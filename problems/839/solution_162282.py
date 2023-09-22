def carros(num_pessoas, capacidade = 5):
    num_carros = 0
    
    if num_pessoas % capacidade == 0:
        num_carros = num_pessoas / capacidade
    else:
        num_carros = 1 + num_pessoas / capacidade
        
    return int(num_carros)