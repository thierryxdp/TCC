# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    """Essa função recebe as dimensões de um colchão e as medidas da 
    altura e largura de uma porta e calcula se o colchão consegue passar
    pela porta. lista,int->bool"""
    areacolchao = 2*(medida[0]*medida[1]+medida[1]*medida[2])
    areaporta = H*L
    return areacolchao<areaporta