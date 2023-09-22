# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas, H, L):
    a,b,c = medidas
    if a <= H and b <= H or a <= L and b <= L or c <= H and c <= L:
        return true
    else:
        return false