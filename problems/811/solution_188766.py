# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas, H, L):
    #medidas comprimento altura largura
    if medidas[3] <= L and (medidas[1] <= H):
        return True
    else:
        return False