# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    '''Função que recebe as dimensões das portas da casa do usuário e as dimensões do colchão e retorna se o colchão passa ou não'''
	'''list, int, int --> bool'''
    x=medidas[0]
    y=medidas[1]
    z=medidas[2]
    if x <= H and x <= L:
        if y <= L or y <= H:
            return True
        else:
            return False
    elif x < L:
        if y < H:
            return True
    else:
        return False