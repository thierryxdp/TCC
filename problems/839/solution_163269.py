def carros(num_pessoas, capacidade = 5): # adicionei um argumento default para capacidade caso não seja fornecido
    return int(num_pessoas/capacidade) + 1