#Start your python function here
def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''

# primeira etapa - extrair as coordenadas das tuplas recebidas como argumentos
    #x_inf_esq1, y_inf_esq1, x_sup_dir1, y_sup_dir1 = ret1
   # x_inf_esq2, y_inf_esq2,  x_sup_dir2, y_sup_dir2 = ret2

# segunda etapa - calculo do resultado
	kx=ret2[2]-ret1[0]
    ky=ret2[3]-ret1[1]
    if( (ky>0 and kx>0) or (ky>0 and kx==0) or (kx>0 and ky<0)):
        return ret1[3]<ret2[1] or ret1[2]<ret2[0]
    elif((kx<0 and ky==0) or (kx<0 and ky<0) or (kx<0 and ky>0)):
        return ret1[3]>ret2[1] or ret1[2]>ret2[0]
    else:
        return True