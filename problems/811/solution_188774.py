# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas, H, L):
    #medidas espessura 0, largura 1, comprimento 2
    #H altura, L largura da porta
    if medidas[2] <= H and medidas[1]<=L:
        return True
    else:
        return False