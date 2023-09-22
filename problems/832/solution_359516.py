def eh_quadrada(m):
    '''recebe uma matriz, e retorna True se ela for quadrada,
    e False se não for quadrada; list -> bool'''
    if m == []:
        return True
    for i in m:
        if len(i) != len(m):
            return False
    	else:
			return True