def colchao(med,h,l):
    '''Função que dado as dimensoes de um colchao e as 
    dimensões de uma porta, retorna se o colchao passa
    ou nao na porta
    ass: list[int,int,int],int,int --> bool
    testes:
	'''
    if h >= l:
    	if (med[0]>h and med[1]>h) or med[0]>h and med[2]>h or (med[1]>h and med[2]>h):
        	return False
    if l > h:
    	if (med[0]>l and med[1]>l) or (med[0]>l and med[2]>l) or (med[1]>l and med[2]>l):
            return False  
    return True