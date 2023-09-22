# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas, H, L):
    ''' Função que retorna se o colchão passa pela porta de acordo com as suas medidas
    list, float, float -> bool
    '''
    if medidas[1] <= H:
       return True
    if medidas[1] <= L:
       return True
    if medidas[2] <= H:
       return True
    if medidas[2] <= L:
       return True
    else:
       return False