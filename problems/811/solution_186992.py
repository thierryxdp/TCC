def colchao(medidas,H,L):
    if medidas[2]<=H:
        return True
    elif medidas[1]<=H:
        return True
    elif medidas[1]>H and (medidas[1]*medidas[2])<H*L:
        return True
    else:
        False

# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis