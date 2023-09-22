# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    """dadas as dimensões do colchão e da porta, a função retorna True
    se ele consegue atravessá-la e False se não consegue.
    list, int, int-->bool
    
    Parâmetros
    medidas: dimensões do colchão, listadas da menor para a maior
    H: altura da porta
    L: largura da porta"""
    if medidas[0]<=H and medidas[1]<=L:
        return True
    elif medidas[1]<=H and medidas[0]<=L:
        return True
    else:
        return False