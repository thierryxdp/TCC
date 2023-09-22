def carros(num_pessoas, capacidade = 5): # adicionei um argumento default para capacidade caso não seja fornecido
    num_carros = num_pessoas/capacidade
    
    return int(num_carros +1)