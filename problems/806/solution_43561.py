def colisao(retA,retB):
    '''funçao que retorna com a resposta em bool se teve ou nao colisao nas coordenadas de entrada''' 
    '''Tupla->bool'''
    x1,y1,X1,Y1=retA 
    x2,y2,X2,Y2=retB 
    if X1<x2 and x1<X2:
        return False