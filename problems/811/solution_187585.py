# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    """função que calcula as medidas de um colchão e compara 
    com as medidas da porta para verificar se o colchão
    passa por ela"""
     a, b, c = medidas
    return (a <= H and b <= L) or (a <= L and b <= H) or (a <= H and c <= L) or (a <= L and c <= H) or (c <= H and b <= L) or (c <= L and b <= H)