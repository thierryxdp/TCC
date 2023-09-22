def colisao_v1(ret1,ret2):
# primeira etapa - extrair as coordenadas das tuplas recebidas como argumentos
    x_inf_esq1, y_inf_esq1, x_sup_dir1, y_sup_dir1 = ret1
    x_inf_esq2, y_inf_esq2, x_sup_dir2, y_sup_dir2 = ret2
# segunda etapa - calculo do resultado
# se o extremo mais a direita de um retangulo esta antes do
# extremo mais a esquerda do outro nao tem problema no eixo x
    if x_sup_dir2 < x_inf_esq1 or x_sup_dir1 < x_inf_esq2:
        xok = True
    else:
        xok = False
# se o extremo mais acima de um retangulo esta abaixo do
# extremo mais abaixo do outro nao tem problema no eixo y
    if y_sup_dir2 < y_inf_esq1 or y_sup_dir1 < y_inf_esq2:
        yok = True
    else:
        yok = False
# basta que um dos 2 esteja ok para que nao haja intersecao
    if xok or yok:
        return False #nao ha intersecao
    else:
        return True