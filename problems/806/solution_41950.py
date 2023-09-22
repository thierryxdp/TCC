def colisao(x1,y1,x2,y2,x3,y3,x4,y4):
    """a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''
    (x1,y1)->vertice inferior esquerdo do primeiro retangulo
    (x2,y2)->vertice superior direito do primeiro retangulo
    (x3,y3)->vertice inferior esquerdo do segundo retangulo
    (x4,y4)->vertice inferior esquerdo do segundo retangulo"""
    if y2>y4>y1