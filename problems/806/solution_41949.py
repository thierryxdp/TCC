def colisao(x1,y1,x2,y2):
    """a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''
    (x1,y1)->vertice inferior esquerdo do retangulo
    (x2,y2)->vertice superior direito do retangulo"""
    if x2>x1 or x1>x2:
    return False
    if y2>y1 or y1>y2:
    return False
	else:
        return True