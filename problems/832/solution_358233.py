def eh_quadrada(lista):
    '''Função que identifica se uma matriz é quadrada ou não.
    lista->boolean'''
       
    for i in range(len(lista)):
    	
        for j in range(len(lista[i])):
            
          	if len(lista)==len(lista[i]):
                   return True