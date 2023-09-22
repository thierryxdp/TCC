def colchao(medidas, H, L):
    """Função que define se o colchão consegue passar pela porta da casa
       list(int, int, int), int, int -> bool
       
       Parameters
       A == parâmetro numérico que representa a espessura do colchão
       B == parâmetro numérico que representa a largura do colchão
       C == parâmetro numérico que representa a altura do colchão 
       H == parâmetro numérico que representa a altura da porta
       L == parâmetro numérico que representa a largura da porta"""
    [A,B,C] = medidas
    return (B <= L and A <= H) or (B <= H and A<= L) or (C <= H and B <= L) or (C <= H and A <= L)