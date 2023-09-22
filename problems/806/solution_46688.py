#Start your python function here
def colisao(ret1,ret2):
    '''Esta função verifica se dois retângulos se colidiram. Na entrada, são
passadas duas tuplas referentes aos vértices de x e y dos dois pontos de cada
retângulo. Os valores passados devem ser do ponto mais à esquerda e mais baixo;
e mais à direita, mais alto. A função retorna. A função verifica a distância seja
na altura ou na largura entre o ponto mais alto do retângulo mais à esquerda com
o ponto mais baixo, mais à esquerda do retângulo mais à direita. Caso eles estejam
na mesma distância em relação ao eixo x, é verificado a altura entre os pontos citados.
O retorno será True se houver colisão; e False se não houver.
tuple,tuple --> bool'''

# primeira etapa - extrair as coordenadas das tuplas recebidas como argumentos
    x_inf_esq1, y_inf_esq1, x_sup_dir1, y_sup_dir1 = ret1
    x_inf_esq2, y_inf_esq2,  x_sup_dir2, y_sup_dir2 = ret2
    

# segunda etapa - calculo do resultado
    if x_inf_esq1 < x_inf_esq2:
        if y_sup_dir1 < y_inf_esq2:
            return False
        elif x_sup_dir1 < x_inf_esq2:
            return False
        else:
            return True

    if x_inf_esq1 > x_inf_esq2:
        if y_sup_dir2 < y_inf_esq1:
            return False
        elif x_sup_dir2 < x_inf_esq1:
            return False
        else:
            return True

    else:
        if y_inf_esq1 < y_inf_esq2:
            if y_sup_dir1 < y_inf_esq2:
                return False
            else:
                return True
        if y_inf_esq1 > y_inf_esq2:
            if y_sup_dir2 < y_inf_esq1:
                return False
            else:
                return True
        else:
            return True