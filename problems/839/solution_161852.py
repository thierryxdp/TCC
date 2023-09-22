def carros(n_pessoas, cap_carros = 5):
    if(n_pessoas % cap_carros == 0):
    	return n_pessoas / cap_carros
    else:
        return (n_pessoas // cap_carros) + 1