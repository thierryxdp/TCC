# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    """funcao...
    lista, int, int -> bool"""
    a=medidas[0]
    b=medidas[1]
    c=medidas[2]
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