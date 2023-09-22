def colchao( medidas, H , L):
    ''' [H - altura da porta / L - largura da porta]
        função pré-definida para avaliar se um colchão com medidas(A,B,C)
        pode ser transportado por portas de medidas H e L
        [list,int,int-->bool]'''
    
    A , B , C = medidas
    if A*B < H*L:
        return True
    else:
        return False