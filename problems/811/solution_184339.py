# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    """funcao...
    lista, int, int -> bool"""
    medidas[0]=a
    medidas[1]=b
    medidas[2]=c
    if a<=H and b<=L:
        return True
    elif a<=H and c<=L:
        return True
    elif b<=H and a<=L:
        return True
    elif b<=H and c<=L:
        return True
    elif c<=H and a<=L:
        return True
    elif c<=H and b<=L:
        return True
    else:
        return False