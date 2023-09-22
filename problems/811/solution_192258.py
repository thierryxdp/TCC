def colchao (medidas,H,L):
    '''diz se um colchão passa pela porta, sendo H(altura porta), L(largura porta), medidas(lista com medidas do colchão)'''
     [a,b,c]=medidas
        if b<L and a<H:
        	return True
        if a<L and b<H:
        	return True
        else:
            return False