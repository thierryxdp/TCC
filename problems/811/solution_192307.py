# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    '''Essa função informa se uma cama passa pela porta, dadas suas medidas
    lista, int, int -> dicionário'''
    return medidas[0]<=L and medidas[1]<=H or medidas[0]<=H and medidas[1]<=L