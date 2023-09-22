def colchao(medidas,H,L):
    #essa função dirá se um colchao atravessara uma porta atraves de
    #suas medidas e o tamanho da porta
    x1=min(medidas)
    l1=[H,L]
    t=min(l1)
    if(x1<t):
        medidas.remove(min(medidas))
        x2=min(medidas)
        l1.remove(min(l1))
    	if(x2<min(l1)):
            return True
    else:
     	return False