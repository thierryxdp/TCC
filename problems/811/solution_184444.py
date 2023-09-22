# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    if (max(H,L)<medidas[0]):
        return False
    elif(max(H,L)<medidas[1]):
        return False
    else:
        return True