'''função que diz o numero de carros em função do número de pessoas.'''
def carros (p,c):
	if p/c!=0:
        return math.ceil (p/c)
    else:
        return (p/c)