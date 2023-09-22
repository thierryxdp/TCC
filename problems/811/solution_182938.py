"""Na função abaixo, primeiramente são definidas as medidas do colchao por (a,b,c), sendo que estas representam a altura, o comprimento
a largura; não necessariamente nesta ordem, pois foi explicitado na questão que João poderia rotacionar o colchão. Adiante, basta serem
informados os valores do colchão e da porta (altura e largura). Por fim, caso os dois últimos valores do colchão forem maiores do que
os da largura e altura da porta, retornará False; porém se pelo menos um dele foi menor ou igual aos da porta, a resposta será True."""

def medidas(a,b,c):
    return (a,b,c)

def colchao (medidas, H, L):
    if medidas[1]>H and L>medidas[2]:
        return True
    
    if medidas[1]>H and medidas[2]>L:
        return False
   
    if H>medidas[1] and L>medidas[2]:
        return True
    
    if H>medidas[1] and medidas[2]>L:
        return True
    
    if medidas[1] == H and medidas[2]>L:
        return True