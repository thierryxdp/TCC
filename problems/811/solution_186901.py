def colchao(medidas,H,L):
    #essa função dirá se um colchao atravessara uma porta atraves de
    #suas medidas e o tamanho da porta
    x1=min(medidas)
    t=min(H,L)
    if(x1<t):
            list.remove(min(medidas))
            x2=min(medidas)
    if(x2<L):
            return True
    else:
     	return False