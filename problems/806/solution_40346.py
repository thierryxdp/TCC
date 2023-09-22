def colisao(ret1, ret2):
    '''Entrada:
    	É fornecido as condenadas(int) dos vértices sup e inf de cada retangulo ---> tuple
    Saída:
        Retorna se eles estão em contato ---> bool
    '''
    
  		xi1= ret1[0]
  		yi1= ret1[2]
    	xs1= ret1[4]
    	ys1= ret1[6]
    	xi2= ret2[0]
    	yi2= ret2[2]
    	xs2= ret2[4]
    	ys2= ret2[6]
    
    if (xs1-xi2) >= 0 and (ys1-yi2) >= 0 and (xs2-xi1) >= 0 and (ys2-yi1) >= 0:
        return True
    else:
        return False