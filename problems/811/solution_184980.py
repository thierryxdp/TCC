def colchao(medidas,H,L):
        '''teste'''

        dimensoes=str(medidas)
        dimensoes=str.split(dimensoes)
        B=int(str.strip(dimensoes[1],','))
        
        if (B<=H):
                return True
        else:
                return False