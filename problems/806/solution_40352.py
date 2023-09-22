def colisao(ret1, ret2):
    '''Entrada:
    	É fornecido as condenadas(int) dos vértices sup e inf de cada retangulo ---> tuple
    Saída:
        Retorna se eles estão em contato ---> bool
    '''
  	x1i = int(ret1[0])
  	y1i = int(ret1[2])
   	x1s = int(ret1[4])
   	y1s = int(ret1[6])
    x2i = int(ret2[0])
    y2i = int(ret2[2])
    x2s = int(ret2[4])
    y2s = int(ret2[6])
    
    if (x1s-x21) >= 0 and (y1s-y2i) >= 0 and (x2s-x1i) >= 0 and (y2s-y1i) >= 0:
        return True