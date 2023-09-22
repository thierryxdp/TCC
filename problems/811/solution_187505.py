# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    
    if medidas[0] and medidas[1] and medidas[2] >= H:
        return False
    elif medidas[0] and medidas[1] and medidas[2] >= L:
        return False
    elif medidas[0] and medidas [1]>= H:
    	return False
    elif medidas[0] and medidas [1]>= L:
        return False
    elif medidas [1] and medidas [2]>= H:
        return False
    elif medidas [1] and medidas [2]>= H:
        return False
    elif medidas[0] and medidas[2]>= H:
        return False
    elif medidas[0] and medidas[2]>= L:
        return False
    else:
        return True