# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    medidas = [0,1,2]
    
    if (medidas[2] and medidas[1]) > (H and L) or (medidas[2] and medidas[0]) > (H and L)  or (medidas[1] and medidas[0]) > (H and L):
        return True
    else:
        return False