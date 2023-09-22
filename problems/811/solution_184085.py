# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    '''função que dadas as medidas de um colchão e as dimensões de uma porta, retorna True se o colchão passa por ela
    e False se não passa; list,int,int-> bool'''
    if medidas[1]<=H:
        return True
    else:
        return False