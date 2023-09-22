def colchao(medidas,h,l):
    colchao = medidas
    porta = h,l
    if colchao[1]>porta[0] and colchao[1]>porta[1]:
        return False
        else:
            return True