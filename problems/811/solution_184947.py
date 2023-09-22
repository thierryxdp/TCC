# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    """ função que calcule e retorne a dimensão do colchão para vê se ele consegue passar pela porta dadas as informações da entrada; list, int, int -> bool"""
    a=medidas[0]
    b=medidas[1]
    if (b<=H and a<=L) or (b<=L and a<=H):
        return True
    else:
        return False