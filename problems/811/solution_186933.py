def colchao(medidas,H,L):
    '''a função recebe os valores da medida do colchão e 
    da porta e retorna se é possível passar por ela ou não
    medidas = [a,b,c] em cm, ordem crescente
    H (altura) e L(largura) tamanho da porta
    [float],int,int->bool'''
    if H > L:
        if medidas[0] <= L:
            return (medidas[1]or medidas[2]) <= H
    	else:
        	return L > medidas[0]
    else:
        if medidas[0] <= H:
            return (medidas[1]or medidas[2]) <= L
    	else:
        	return H > medidas[0]