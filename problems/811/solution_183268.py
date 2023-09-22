# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao (medidas, H, L):
    """ Função que dadas as medidas do colchao e da porta, retorna se o colchao passa pela porta;
        list, int, int -> bool."""
    if (H >= medidas [1] and L >=medidas [0] and medidas [2] > H and medidas [2] > L):
        return True
    else:
        return False