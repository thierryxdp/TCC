# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colcha(medidas,H,L):
    """Função que informa se um colchão com proporções A x B x C (dadas em uma lista), consegue passar através da porta de sua casa com altura H e largura L;
       list, float,float -> bool"""
    espessura_colchao = medidas[0]
    largura_colchao = medidas[1]
    altura_colchao = medidas[2]
    if (altura_colchao < H and largura_colchao < L) or (largura_colchao<H):
        return True
    else:
        return False