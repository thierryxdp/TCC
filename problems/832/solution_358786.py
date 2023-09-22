def eh_quadrada(m):
    '''recebe uma matriz e identifica se ela eh quadrada ou nao
    lista->bool'''
   
	if (len(m)==len(m[0])):
        return True
    else:
        return False