def carros(qtd,places=5):
    if qtd < 6:
        return qtd
    else:
        if qtd//places == 0:
        	return qtd//places
        else:
            qtd//places !=0
        	return (qtd//places)+1