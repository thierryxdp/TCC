# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao (medidas,H,L):
    '''Dadas as medidas de um colchão e as medidas da porta, retorna True quando o colchão passa pela porta e False quando não passa.
    list, int, int -> bool'''
    if medidas[0] < L and medidas[1] < H:
        return True
    else:
        return False