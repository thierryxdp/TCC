def colchao(lista,h,l):
    
    ''' A função recebe uma lista de tres valores como paramentro 
  		representando as dimenssões do colchão do menor para o maior, a altura(h) e 
   		e a largura (l) da porta; list, float, float -> bool
    '''
    	
    if lista[1]<=h or lista[2]<l: 
        return True
    
    else :
        return False