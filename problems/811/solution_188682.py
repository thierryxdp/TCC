# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    medidas = [0,1,2]
    
    if (medidas[2] <= H) and (medidas[1] <= L):
        return True
    else:
        return False