def colisao(ret1,ret2):
    '''Função que recebe duas tuplas com quatro valores, representando as 
     coordenadas de um retângulo e retorna se eles colidem ou não, sendo true para casos de colisão e false para casos
     onde não se tocam.
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     assinatura tuple, tuple --> bool
     testes:
     colisao((1,1,2,2),(2,2,4,4)) == True
     colisao((1,1,2,2),(4,4,6,6)) == False

     '''
    x_inf_esq1, y_inf_esq1, x_sup_dir1, y_sup_dir1 = ret1
    x_inf_esq2, y_inf_esq2,  x_sup_dir2, y_sup_dir2 = ret2
    if x_sup_dir2 < x_inf_esq1 or x_sup_dir1 < x_inf_esq2:
        return False
    if y_sup_dir2 < y_inf_esq1 or y_sup_dir1 < y_inf_esq2:
        return False
    else:
        return True