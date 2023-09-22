def carros(num_pessoas, capacidade = 5):
    num_carros = 0
    while(num_carros < num_pessoas):
        num_carros *= capacidade
    	
    return int(num_carros)