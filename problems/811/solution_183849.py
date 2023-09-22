# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas, H,L):
    medidas=[medidas[0],medidas[1],medidas[2]]
    Area_porta=H*L
    if (medidas[0] and medidas[1])<=(H and L):
         return True
    elif (medidas[2] and medidas[1]) <= (H and L):
        return True
    else:
        return False