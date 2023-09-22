# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas, H, L):
    """Função que avalia se o colcão consegue passar pela porta da casa
    A = espessura do colchão
    B = largura do colchão
    C = altura do colchão
    H = altura da porta
    L = largura da porta
    list(int, int, int), int, int -> bool"""
    [A, B, C] = medidas 
    return (B <= L and A <= H) or (B <= H and A <= L) or (C <= H and B <= L) or (C <= H and A <= L)