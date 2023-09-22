#Função que detecta colisão entre os retangulos. 
#tupla,tupla->bool
def colisao(ret1,ret2):
    if (ret1[2] < ret2[0] or ret2[2] < ret1[0] or ret1[3] < ret2[1] or ret2[3] < ret1[1] or ret1[0] > ret2[2] or ret2[0] > ret1[2] or ret1[1] > ret2[3] or ret2[1] > ret1[3]):
        return False
    else:
        return True