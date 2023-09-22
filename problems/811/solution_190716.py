""" 
Nesta função, utilizamos 2 formas para descobrir se o colchão passaria ou não,
primeiro vamos ver se a maior medida do colchão é menor que os dois lados da
porta, caso esse seja o caso, ela passa, caso a segunda maior medida seja 
maior que as duas medidas da porta, ele não passa. Nos outros casos, decidiremos
pela área das 2 duas medidas do colchão (a partir da altura x lados) comparadas
à área da porta. 
list, int, int -> bool
"""
def colchao(medidas, H, L):
    medida1 = medidas[0]*medidas[1]
    medida2 = medidas[0]*medidas[2]
    areaP = H*L
    if medidas[2] <= H and medidas[2] <= L:
        return True
    elif medidas[1] > H and medidas[1] > L:
        return False
    elif medida1 <= areaP:
        return True
    elif medida2 <= areaP:
        return True
    else:
        return False