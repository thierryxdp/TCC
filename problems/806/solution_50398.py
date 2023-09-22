#Start your python function here
def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''

# primeira etapa - extrair as coordenadas das tuplas recebidas como argumentos
    x_inf_esq1, y_inf_esq1, x_sup_dir1, y_sup_dir1 = ret1
    x_inf_esq2, y_inf_esq2,  x_sup_dir2, y_sup_dir2 = ret2

# segunda etapa - calculo do resultado
def colisao(ret1,ret2):
    """ - """

    xinfesq = (ret1[0])
    xinfdir = (ret1[1])
    xsupesq = (ret1[2])
    xsupdir = (ret1[3])

    yinfesq = (ret2[0])
    yinfdir = (ret2[1])
    ysupesq = (ret2[2])
    ysupdir = (ret2[3])

    list1 = []
    list2 = []

    contador1 = xinfesq
    contador2 = yinfesq

    while contador1 < xsupesq:
        list1.append(contador1)
        contador1 = contador1 + 1

    while contador2 < ysupesq:
        list2.append(contador2)
        contador2 = contador2 + 1

    for i in list1:
        if i in list2:
            return true
        else:
            return false