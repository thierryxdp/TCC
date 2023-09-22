import.math
def colisao(ret1,ret2):
    ''' Essa função recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se há colisão entre os 2 retângulos e False, caso contrário;
     tuple, tuple --> bool. '''
     inter = []
        for x in ret1:
            for y in ret2:
                if x == y:
                    inter.append(x)
        return inter