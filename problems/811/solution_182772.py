# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis

def colchao(medidas, H, L):
    if H > L:
        H, L = L, H
 
    medidas = sorted(medidas)
    
    return not(medidas[0] >= L) and not(medidas[1] >= H)