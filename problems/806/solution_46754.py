def colisao (R1, R2):
    '''função que dada as coordenadas dos vétices que vão da esquerda pra direita
(x1->x2, x3->x4) e de baixo para xima (y1->y2 e y3->y4) de dois retangulos
em duas tuplas com quatro valores cada tupla, devolve True caso haja colisão
entre os retângulos e False caso não haja colisão
: tuple, tuple --> bool'''
#R1=(x1,y1,x2,y2)
#R2=(x3,y3,x4,y4)
    
    x1=R1[0]
    y1=R1[1]
    x2= R1[2]
    y2=R1[3]
    
    x3= R2[0]
    y3= R2[1]
    x4= R2[2]
    y4=R2[3]

    if (x2<x3) or (x4<x1) or (y2<y3) or (y4<y1):
      return False
    else:
        return True