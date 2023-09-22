# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao (medidas,H,L):
    '''Dadas as medidas de um colchão e as medidas da porta, retorna True quando o colchão passa pela porta e False quando não passa.
    list, int, int -> bool'''
    l, h, c = medidas
    if l <= L and h <= H:
        return True
    else:
        return False