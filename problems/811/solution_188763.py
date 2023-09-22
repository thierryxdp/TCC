# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(dimensoes,H,L):
    if dimensoes[0]<=H and dimensoes[1]<=L:
        return True
    elif dimensoes[0]<=L and dimensoes[1]<=H:
        return True
    else:
        return False