#Start your python function here
def colisao(retangulo1,retangulo2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''
    if ( ( r e t a n g ul o 1 .X + r e t a n g ul o 1 . Largura > r e t a n g ul o 2 .X)or( r e t a n g ul o 1 .X < r e t a n g ul o 2 .X)or( r e t a n g ul o 1 .Y + r e t a n g ul o 1 . Al tu r a > r e t a n g ul o 2 .Y) or( r e t a n g ul o 1 .Y < r e t a n g ul o 2 .Y) ):
        return True