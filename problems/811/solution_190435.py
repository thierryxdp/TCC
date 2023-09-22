def colchao(dimensoes,H,L):
        if dimensoes[1]<=L and dimensoes[0]<=H:
            return True
        if dimensoes[0]<=L and dimensoes[2]<=H:
            return True
        if dimensoes[2]<=L and dimensoes[1]<=H:
            return True
        else:
            return False