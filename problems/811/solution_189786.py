# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    if min(medidas[1], medidas[2]) > max(H,L):
        return False
    else:
        return True