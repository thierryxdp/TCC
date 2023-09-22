#Start your python function here
def colisao(r1,r2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''
    #(x_inf_esq1, y_inf_esq1, x_sup_dir1, y_sup_dir1)=ret1
    #(x_inf_esq2, y_inf_esq2,  x_sup_dir2, y_sup_dir2)=ret2
   	if not(int(r2[2])<int(r1[0]) or int(r1[2])<int(r2[0])) and not(int(r2[3])<int(r1[1]) or int(r1[3])<int(r2[1])):
        return True
    else: 
        return False