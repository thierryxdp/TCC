# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas, H, L):
    if max(H, L) >= min(medidas[1:]):
        return True
    return False