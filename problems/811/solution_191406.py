def colchao(med,h,l):
    '''# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis'''
    if h >= l:
    	if (med[0]>h and med[1]>h) or med[0]>h and med[2]>h or (med[1]>h and med[2]>h):
        	return 'k'
    if l < h:
    	if (med[0]>l and med[1]>l) or (med[0]>l and med[2]>l) or (med[1]>l and med[2]>l):
            return False  
    return True