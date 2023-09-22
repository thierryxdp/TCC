# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    '''calcula se o colchão passará ou não pela porta. list,int,int->bool'''
    if medidas[0]>L:
        return False
    if medidas[1]>H:
        return False
    else:
        return True