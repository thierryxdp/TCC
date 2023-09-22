def colchao(medidas,alturaH,larguraL):
    
    porta=[alturaH,larguraL]
    
    if medidas[0]<= min(porta) and medidas[1]<= max(porta):
        return True
    else:
        return False