def carros(cap_carro=5, n_pessoas):
    if(n_pessoas % cap_carros == 0):
    	return n_pessoas / cap_carros
    else:
        return (n_pessoas // cap_carros) + 1