# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    if max(medidas) > max(H,L):
        return False
    else:
        return True