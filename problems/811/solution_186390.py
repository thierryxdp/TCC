# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colcha(medidas,H,L):
    """Função que informa se um colchão com proporções A x B x C (dadas em uma lista), consegue passar através da porta de sua casa com altura H e largura L;
       list, float,float -> bool"""
    espessura = medidas[0]
    largura  = medidas[1]
    altura = medidas[2]
    if (altura < H and largura < L) or (largura < H):
        return True
    else:
        return False