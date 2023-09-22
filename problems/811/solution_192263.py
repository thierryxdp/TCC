def colchao (medidas,H,L):
    '''diz se um colchão passa pela porta, sendo H(altura porta), L(largura porta), medidas(lista com medidas do colchão)'''
        medidas=[a,b,c]
       if b<L and a< H:
        	return True
       if a<L and b< H:
        	return True
       else:
            return False