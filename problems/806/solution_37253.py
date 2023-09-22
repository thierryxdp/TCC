def colisao(coordRet1, coordRet2):
    '''Recebe duas tuplas com quatro valores inteiros cada uma, representando as 
    coordenadas dos vértices inferior esquerdo e superior direito do primeiro 
    retângulo e do segundo retângulo, nessa ordem, e devolve True se ha colisão 
    entre os 2 retângulos e False, caso contrário.
    tuple, tuple --> bool
    
    Explicação: Primeiro extrai as coordenadas das tuplas recebidas.
    Depois identifica os casos em que não ocorre colisão (que são quando o vértice 
    inferior do retângulo 2 está acima ou à direita do vértice superior do retângulo 1,
    ou quando o vértice superior do retângulo 2 está abaixo ou à esquerda do vértice 
    inferior do retângulo 1) e retorna False para estes.
    Por último, identifica os casos em que ocorre colisão retornando True pra estes'''
    
   # primeira etapa - extrair as coordenadas das tuplas recebidas como argumentos
    x_inf_esq1 = coordRet1[0]
    y_inf_esq1 = coordRet1[1]
    x_sup_dir1 = coordRet1[2]
    y_sup_dir1 = coordRet1[3]
    

    x_inf_esq2 = coordRet2[0]
    y_inf_esq2 = coordRet2[1]
    x_sup_dir2 = coordRet2[2]
    y_sup_dir2 = coordRet2[3]

    # segunda etapa - calculo do resultado
    
    if x_inf_esq2 > x_sup_dir1 or y_inf_esq2 > y_sup_dir1 or x_sup_dir2 < x_inf_esq1 or y_sup_dir2 < y_inf_esq1:
        return False
    else:
        return True