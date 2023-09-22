# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas, H, L):
    [A, B, C] = medidas
    if (A <= H and B <= L) or (B <= H and A <= L):
        return True
    if (A <= H and C <= L) or (C <= H and A <= L):
        return True
    if (B <= H and C <= L) or (C <= H and B <= L):
        return True
    else:
        return False