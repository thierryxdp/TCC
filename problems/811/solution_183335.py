# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    """Funcao que, dado uma lista (medidas) com os comprimento A, B, C do colchao em cm de tamanha, altura e largura, passa ou não pela porta (HxL)da casa dele.
    list, int, int --> bool"""
    if medidas[1] <= H and medidas [0] <=L:
        return True
    else:
        return False