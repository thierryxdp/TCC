# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas, H, L):
    m1 = medidas[0]
    m2 = medidas[1]
    
    if (m2 <= H and m1 <= L) or (m2 <= L and m1 <= H):
        return True
    else:
        return False