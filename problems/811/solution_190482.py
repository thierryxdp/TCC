# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao (medidas,H,L):
    '''Dadas as medidas de um colchão e as medidas da porta, retorna True quando o colchão passa pela porta e False quando não passa.
    list, int, int -> bool'''
    a = medidas[0]
    b = medidas[1]
    c = medidas[2]
    if a > L or b > L or c > L and a > H or b > H or c > H:
        return False
    else:
        return True