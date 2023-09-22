# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas, H, L):
    ''' Verifica se o colchao a ser comprado passa pela porta,
    dados suas dimenções 
    lis, int, int -> bool'''
    return medidas[2] <= H or medidas[2] <= L