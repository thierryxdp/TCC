#Start your python function here
def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''
    var=rect1 = {x: 5, y: 5, width: 50, height: 50}
var=rect2 = {x: 20, y: 10, width: 10, height: 10}

if (rect1.x < rect2.x + rect2.width and
   rect1.x + rect1.width > rect2.x and
   rect1.y < rect2.y + rect2.height and
   rect1.y + rect1.height > rect2.y) :
    return True
else:
    return False