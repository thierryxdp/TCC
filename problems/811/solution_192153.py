# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,alturaH,larguraL):
    """ função que dadas as medidas da colchao, altura e largura da porta, retorna;
        se o colchao consegue passar pela porta;
        list,int,int-> bool"""
    a=[alturaH,larguraL]
    
    if medidas[0]<= min(a) and medidas[1]<= max(a):
        return True
    else:
        return False