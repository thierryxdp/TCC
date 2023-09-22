def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''

# primeira etapa - extrair as coordenadas das tuplas recebidas como argumentos
    borda_esquerda1, borda_inferior1, borda_direita1, borda_superior1 = ret1
    borda_esquerda2, borda_inferior2,  borda_direita2, borda_superior2 = ret2
    if borda_direita1>borda_esquerda2 or borda_esquerda1<borda_direita2 and borda_inferior1<borda_superior2 and borda_superior1>borda_inferior2:
        return True
    else:
        return False
# segunda etapa - calculo do resultado