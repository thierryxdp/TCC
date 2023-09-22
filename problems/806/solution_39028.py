#Start your python function here
def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos 1,y1,x2,y2 e x3 ,y3,x4,y4 do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''
    t1=[x1,y1,x2,y2]
    t2=[x3,y3,x4,y4]
    if t1[x2] == t2[x3] and t2[x4] == t1[x1] and t1[y2] == t2[y3] and t2[y4] == t1[y1]:
        return True