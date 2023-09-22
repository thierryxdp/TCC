# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    ''' dadas as medidas crescentemente de um colchao 
    qualquer, e as altura (H) e a largura(L) das portas
    de uma casa a funcao retornara se o colchao entra (True)
    ou nao entra (False) numa casa (list, float, float -> bool)'''
    if medidas[1]<=H or medidas[1]<=L and medidas[0]<L:
        return True
    else:
        return False