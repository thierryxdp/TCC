#Start your python function here
def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''

# primeira etapa - extrair as coordenadas das tuplas recebidas como argumentos
    # O x e y minúsculos significam que são os inferiores e o X e Y maiúsculos são os superiores
    x1, y1, X1, Y1 = ret1  
    x2, y2, X2, Y2 = ret2

# segunda etapa - calculo do resultado
    b=(X1-x1)
    h=(Y1-y1)
    B=(X2-x2)
    H=(Y2-y2)
    x1<=b<=X1
    y1<=h<=Y1
    X2<=B<=X2
    Y2<=H<=Y2
    if (B==b and H==h):
        return 'True'
    if (B!=b or H!=h):
        return 'False'