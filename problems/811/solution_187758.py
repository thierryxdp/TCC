# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    A,B,C = medidas
    if B > H or C<L:
        return False
    else:
        return True