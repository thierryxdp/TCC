# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas, H, L):
    """Informa se o colchao passa pela porta"""
    return (medidas[0]<L and medidas[1]<H) or (medidas[0]<H and medidas[1]<L)