def eh_quadrada(m):
    if len(m) == 0:
      	return True
	else:
     	if len(m) == len(m[0]):
        	return True
     	else:
        	return False
'''
    função booleana chamada eh_quadrada para identificar se uma matriz é quadrada.
    OBS:uma matriz vazia (sem nenhuma linha nem coluna) é considerada quadrada.
    m:list
    return:bool
'''