def carros(qtd,places=5):
    if qtd < places:
        return 1
    else:
        if qtd//places == 0:
        	return qtd//places
        else:
            qtd//places !=0
        	return (qtd//places)+1