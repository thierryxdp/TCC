# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    '''Essa funçao..
    lista, int, int -> bool'''
    if medidas == H * L:
        return True
    elif medidas > H*L:
        return False