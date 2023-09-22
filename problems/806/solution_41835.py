#Start your python function here
def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''

# primeira etapa - extrair as coordenadas das tuplas recebidas como argumentos
    XP1, YP1, XP2, YP2 = ret1
    XP3, YP3,  XP4, YP4 = ret2
    if [(YP1>YP3 and YP1<YP2) or (YP1<YP3 and YP3<YP4)] and [(XP3<XP1 and XP1<XP4)or(XP1<XP3 and XP3<XP2)]:
     return True
    else:
     return False    
# segunda etapa - calculo do resultado