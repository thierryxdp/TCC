def colchao(medidas,H,L):
    '''A partir das medidas do colchao e da altura H e largura L da porta
    retorna true se é possivel passar o colchao pela porta
    list[int,int,int],int,int -> bool'''
    a,b,c = medidas
    if H>L:
        Maior = H
        Menor = L
    elif L>=H:
        Maior = L
        Menor = H
  
    if a<=b and a<=c:
        	if b<c:
            	return a<=Menor and b<=Maior
        	elif c<=b:
            	return a<=Menor and c<=Maior
    if b<a and b<=c:
        	if a<c:
            	return b<=Menor and a<=Maior
        	elif c<=a:
            	return b<=Menor and c<=Maior
    if c<a and c<b:
        	if a<b:
            	return c<=Menor and a<=Maior
        	elif b<=a:
            	return c<=Menor and b<=Maior