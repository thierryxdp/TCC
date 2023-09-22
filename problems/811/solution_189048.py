def colchao(medidas,h,l):
    porta=[[medidas[0],medidas[1],medidas[2]],h,l]
    if medidas[0]<=h and medidas[1]<=1 or medidas[1]<=h and medidas[0]<=1 or medidas[2]<=h and medidas[1]<=1:
    	return True
    else:
        return False