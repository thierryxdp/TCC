#Start your python function here
def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''
    x1, y1, x2, y2 = ret1
    x3, y3, x4, y4 = ret2
    
    if (x1<x3<x2<x4) and (y3<y4<y1<y2) or (x3<x1<x4<x2) and (y3<y4<y1<y2) or (x3<x1<x4<x2) and (y1<y2<y3<y4)
		or (x1<x3<x2<x4) and (y1<y2<y3<y4) or (x1=x3<x2=x4) and (y1<y2<y3<y4) or (x3=x1<x4=x2) and (y3<y4<y1<y2)
		or (x1<x2<x3<x4) and (y1<y2<y3<y4) or (x3<x4<x1<x2) and (y1<y2<y3<y4) or (x1<x2<x3<x4) and (y3<y4<y1<y2)
		or (x3<x4<x1<x2) and (y3<y4<y1<y2) or (x1<x2<x3<x4) and (y1=y3<y2<y4) or (x3<x4<x1<x2) and (y3=y1<y2<y4)
		or (x1<x2<x3<x4) and (y3<y1<y4<y2) or (x1,x2<x3<x4) and (y1<y3<y2<y4) or (x3<x4<x1<x2) and (y3<y1<y4<y2)
		or (x3<x4<x1<x2) and (y1<y3<y2<y4):
            return False
    if not ((x1<x3<x2<x4) and (y3<y4<y1<y2)) or ((x3<x1<x4<x2) and (y3<y4<y1<y2)) or ((x3<x1<x4<x2) and (y1<y2<y3<y4))
		or ((x1<x3<x2<x4) and (y1<y2<y3<y4)) or ((x1=x3<x2=x4) and (y1<y2<y3<y4)) or ((x3=x1<x4=x2) and (y3<y4<y1<y2))
		or ((x1<x2<x3<x4) and (y1<y2<y3<y4)) or ((x3<x4<x1<x2) and (y1<y2<y3<y4)) or ((x1<x2<x3<x4) and (y3<y4<y1<y2))
		or ((x3<x4<x1<x2) and (y3<y4<y1<y2)) or ((x1<x2<x3<x4) and (y1=y3<y2<y4)) or ((x3<x4<x1<x2) and (y3=y1<y2<y4))
		or ((x1<x2<x3<x4) and (y3<y1<y4<y2)) or ((x1,x2<x3<x4) and (y1<y3<y2<y4)) or ((x3<x4<x1<x2) and (y3<y1<y4<y2))
		or ((x3<x4<x1<x2) and (y1<y3<y2<y4)):
        	return True