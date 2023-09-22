# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    '''
    funcao que dados as medidas 
    retorna se o colchao passa ou nao pela porta
    '''
    if H>medidas[1] or L>medidas[2]:
        return True
    elif H<medidas[1] and L<medidas[2]:
        return False