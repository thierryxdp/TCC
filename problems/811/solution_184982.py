def colchao(medidas,H,L):
        '''Esta função diz se é possível um colchão com as dimensões inseridas (medidas)
		passar por uma porta de altura (H) e largura (L).
        list,int,int -> bool'''

        dimensoes=str(medidas)
        dimensoes=str.split(dimensoes)
        B=int(str.strip(dimensoes[1],','))
        C=int(str.strip(dimensoes[2],']'))
        
        if (B<=H or C<=L):
                return True
        else:
                return False