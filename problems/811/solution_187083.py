# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    """
    Calcula se as dimensões do colchão passam pela porta da casa
    de João;
    lista,int,int -> bool
    """
    if medidas[1] <= H and medidas[2] <= L:
        return True
    elif medidas[1] <= H and medidas[2] > L:
        return True
    else:
        return False