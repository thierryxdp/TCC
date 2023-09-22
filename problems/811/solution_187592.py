# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
     a, b, c = medidas
    if (a <= H and b <= L) or (a <= L and b <= H) or (a <= H and c <= L) or (a <= L and c <= H) or (c <= H and b <= L) or (c <= L and b <= H):
        return true
    else:
        return false