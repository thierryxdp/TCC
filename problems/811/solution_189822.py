# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    '''
    Recebe uma lista medidas com as dimensões do colchao e as dimensões H e L da porta
    e retorna um bool dizendo se o colchao vai passar na porta
    '''
    return medidas[0]<=min(H,L) and medidas[1]<=max(H,L)