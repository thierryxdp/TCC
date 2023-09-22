# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    '''define se o colchao pode passar pela porta dados; int->bool'''
    A,B,C = medidas
    if B > H and C>L:
        return False
    else:
        return True