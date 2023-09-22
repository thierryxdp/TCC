# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis

def colchao(medidas, H, L):
    A = medidas[0]
    B = medidas[1]
    C = medidas[2]
    
    if A <= H and (B <= L or C <= L):
        return True
    if A <= L and (B <= H or C <= H):
        return True
    if B <= L and C <= H:
        return True
    if B <= H and C <= L:
        return True
    return False