def carros(n_pessoas, cap_carro=5):
    if(n_pessoas % cap_carros == 0):
    	return n_pessoas / cap_carro
    else:
        return (n_pessoas // cap_carro) + 1