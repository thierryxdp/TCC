def colchao(medidas,H,L):
        '''teste'''

        dimensoes=str(medidas)
        dimensoes=str.split(dimensoes)
        B=int(str.strip(dimensoes[1],','))
        C=int(str.strip(dimensoes[2],']'))
        
        if (B<=H or C<=L):
                return True
        else:
                return False