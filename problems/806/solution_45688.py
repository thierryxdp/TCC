#Start your python function here
def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''

# primeira etapa - extrair as coordenadas das tuplas recebidas como argumentos
    xinfesq1, yinfesq1, xsupdir1, ysupdir1 = ret1
    xinfesq2, yinfesq2,  xsupdir2, ysupdir2 = ret2
    if (xinfesq1<=xinfesq2<=xsupdir1) and (yinfesq1<=yinfesq2<=ysupdir1):
        return True
    elif (xinfesq1 == xinfesq2) and (yinfesq1>=yinfesq2) and (xsupdir1 >= xsupdir2) and (ysupdir1>=ysupdir2):
        return True
    elif (xinfesq1<=xinfesq2)and(yinfesq1>=yinfesq2)and(xsupdir1<=xsupdir2)and(ysupdir1<=ysupdir2):
            return True  
    else:
        return False