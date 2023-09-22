def colchao(medidas,H,L):
#Passando com face paralela ao chão
	if int(medidas[1])<L or int(medidas[2])<L:
        return False
    else:
        return True
#Passando em pé
	if int(medidas[1]<H or int(medidas[2])<H:
           return False
    else:
           return True