from math import *
def colisao(reta1,reta2):
    '''
     Dado duas tuplas com quatro valores inteiros, cada uma, representando as
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo
     retângulo, determina se ha colisão ou não

    Uso:
    colisao(reta1,reta2)

    Entrada:
    - reta1 (tupla, obrigatório): x1,y1,x2,y2
    - reta2 (tupla, obrigatório): x3,y3,x4,y4

    Saída:
    - Retorna True se ha colisao entre os 2 retangulos ou False caso contrario. (booleana)
     '''
    
    x1,y1,x2,y2 = reta1
    x3,y3,x4,y4 = reta2

    if x2<x3 or x4<x1 or y2<y3 or y4<y1:
        return False
    else:
        return True
# segunda etapa - calculo do resultado