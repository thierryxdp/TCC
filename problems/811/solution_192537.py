# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    '''Dadas as dimenções do colchão e as medidas da porta, retorna true se o colchão passar e false se não passar lista,int,int->bool''' 
    if (medidas[0]<=H or medidas[0]<=L) and (medidas[1]<=L or medidas[1]<=H):
        return True
    else:
        return False