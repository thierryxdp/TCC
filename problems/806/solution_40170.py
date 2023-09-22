#Start your python function here
def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''
    ret1[0]=a
    ret1[1]=b
    ret1[2]=c
    ret1[3]=d
    ret2[0]=e
    ret2[1]=f
    ret2[2]=g
    ret2[3]=h
    if a<=e<=c and b<=f<=d or a<=g<=c and b<=h<=d or e<=a<=g and f<=b<=h or e<=c<=g and f<=d<=h
        return 'True'
    else:
        return 'False'