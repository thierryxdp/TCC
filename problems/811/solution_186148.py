# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    '''
       Função que ao receber uma lista com as dimensões de um colchão em centímetros(AxBxC) , a altura(H) e largura(L) retorna true se o colchao passa pela porta
       ou false caso não consiga passar
       list, int, int -> boolean
    '''
    A=medidas[0]
    B=medidas[1]
    C=medidas[2]
    
    if A<=H and B<=L:
        return True
    elif A<=H and C<=L:
        return True
    elif B<=H and A<=L:
        return True
    elif B<=H and C<=L:
        return True
    elif C<=H and A<=L:
        return True
    elif C<=H and B<=L:
        return True
    else:
        return False