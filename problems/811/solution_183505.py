# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    """medidas do colchao:A,B,C;H:altura da porta;L:Largura da porta"""
    A:int(medidas[0])
    B:int(medidas[2])
    C:int(medidas[4])
    return (A and B and C)<H and (A and B and C)<l