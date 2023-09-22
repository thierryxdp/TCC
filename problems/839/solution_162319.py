def carros(qtd,places=5):
    if qtd <= places and qtd != 0:
        return 1
    elif qtd == 0:
        return 0
    else:
        if qtd//places == 0:
        	return qtd//places
        else:
            qtd//places !=0
        	return (qtd//places)+1