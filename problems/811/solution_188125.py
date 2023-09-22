def colchao(medidas,H,L):
    espessura=medidas[0:1]
    largurac=medidas[1:2]
    alturac=medidas[2:]
    altura=[H]
    largura=[L]
    if  espessura < largura:
        largurac or alturac < altura or largura
        return True
    else:
        return False