# calcula se a área da porta é maio que a área do colchão
# se a altura da porta é maior que a largura do colchão 
def colchao(medidas,H,L):
    """retorna se o colção passa pela porta, de acordo com as medidas do colchão e da porta"""
    m = medidas
    if (m[1]*m[2]) <= (H*L) or m[1] <= H :
        return True
    if (m[1]*m[2]) > (H*L):
        return False