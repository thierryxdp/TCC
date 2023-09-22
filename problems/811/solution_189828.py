def colchao(medidas,H,L):
    '''retorna se o colchão passa pela porta.
    list,int,int -> bool'''
    espessura = medidas[0]
    largura = medidas[1]
    altura = medidas[2]
    if espessura <= H or espessura < L:
        if largura <= H or largura < L:
       	    return True
        else:
            if altura <= H or altura < L:
      	   	    return True
    	    else:
     		    return False