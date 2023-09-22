def colchao(medidas,H,L):
    '''funcao q calcula se o colchao consegue passar pela altura H, e
    largura L de uma porta, e retorna True se passar, ou False se nao passar'''
    medidas.sort()
    if medidas[0] > H:
        if medidas[0] > L:
            return False
        else:
            return True
	elif medidas[1]>H:
        return False
    else:
        return True