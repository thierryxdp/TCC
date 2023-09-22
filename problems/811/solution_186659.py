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
    medidas[0]==A
    medidas[1]==B
    medidas[2]==C
    if (A<=L and B<=H) or (A<=H and B<=L):
        return True
    else:
        return False