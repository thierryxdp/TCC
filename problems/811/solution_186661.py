def colchao(medidas,H,L):
    '''
       Função que recebe uma lista (medidas) com tres
       elementos inteiros A B e C (largura, altura e
       comprimento do colchao respectivamente em 
       centimetros), e dois int (H e L, altura e largura da
       porta respectivamente, em centimetros), e retorna um 
       booleano para dizer se é possivel (True) ou nao 
       (False) passar o colchao pela porta;
       list, int, int -> bool
    '''  
    A=medidas[0]
    B=medidas[1]
    C=medidas[2]
    if (A>L or B>H) or (A>H or B>L):
        return False
    else:
        return True