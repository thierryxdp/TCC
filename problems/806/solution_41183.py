def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''
    #as informações serão estraídas em pares x e y, respectivamente dos pontos onde referenciam em seu nome
    par_inf_esq1=()
    par_inf_esq2=()
    par_sup_dir1=()
    par_sup_dir2=()
    
    par_inf_esq1= par_inf_esq1 + (ret1[0:1],)
    par_inf_esq2= par_inf_esq2 + (ret2[0:1],)
    par_sup_dir1= par_sup_dir1 + (ret1[1:2],)
    par_sup_dir2= par_sup_dir2 + (ret2[1:2],)
    
    if (par_sup_dir2[0] < par_inf_esq1[0] or par_sup_dir1[0] < par_inf_esq2[0]) or (par_sup_dir2[2] < par_inf_esq1[2] or par_sup_dir1[2] < par_inf_esq2[2]):
        return True
    else:
        return False