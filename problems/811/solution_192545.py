def colchao(medidas, H, L):
    '''retorna Trues se o colchao passa e 
    False se o colchao nao passa'''
    if medidas[2] > H:
        if medidas[1] > H:
            return False
        else:
            return True
    else:
        if medidas[1]>L:
            if medidas[0] > L:
            	return False
            else: 
                return True