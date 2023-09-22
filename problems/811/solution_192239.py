def colchao(medidas,h,l):
    medidas.sort()
    
    altura = medidas[0]
    largura = medidas[1]
    comprimento = medidas[2]
    
    if comprimento < h:
        return True
    if largura < h:
        return True