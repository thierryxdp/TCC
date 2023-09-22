# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas, H, L):
    '''
    Esta função recebe as medidas de um colchão, a altura e a largura de uma porta e retorna, um resultado
    do tipo bool, True se o colchão consegue passar pela porta de alguma maneira e False se o colchão não consegue
    passar poela porta de forma alguma.
    
    Parametros
    ----------
    medidas (list) : medidas do colchão em números inteiros (int)
    H (int) : altura da porta
    L (int) : largura da porta
    '''
    if medidas[1] <= L and medidas[0] <= H:
        return True
    elif medidas[0] <= L and medidas[1] <= H:
        return True
    elif medidas[1] <= L and medidas[1] <= H:
        return True
    elif medidas[0] <= L and medidas[2] <= H:
        return True
    else:
        return False