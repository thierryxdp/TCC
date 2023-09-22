def carros(p, c=5):
    """Calcula o numero de carros necessarios para realizar uma viagem dados o numero de pessoas: p
    e a capacidade dos carros: c caso nao sejam usados carros convencionais de 5 lugares """
    i = p//c
    j = p%c
    if j != 0:
        return i + 1
    else:
    	return i