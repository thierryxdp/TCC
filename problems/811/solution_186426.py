def colchao (medidas,H,L):
    """retorna true se o colchão passar pela porta ou false
    se o colchão não passar pela porta"""
    A = medidas[0]
    B = medidas[1]
    C = medidas[2]

    
    if B <= H or C <= H and A < B and A < C:
        return True
    if B <= L or C <= L and A < B and A < C:
        return True
    else: 
        return False# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis