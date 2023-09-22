def colisao(ret1,ret2):
    xie1, yie1, xsd1, ysd1 = ret1
    xie2, yie2, xsd2, ysd2 = ret2
    colidir=not(xsd1<xie2 or xsd2<xie1 or ysd1<yie2 or ysd2<yie1)
    return colidir