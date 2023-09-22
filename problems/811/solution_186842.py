# Função que retorna valores booleanos se o colchão passa ou não pela porta
# lista com as dimensões do colchão em centímetros e dois inteiros H e L
"""lis,int,int--->bool"""
def colchao(medidas,H,L):
    if (medidas[0] <= L) and (medidas[1] <= H):
        return True
    if (medidas[0] <= H) and (medidas[1] <= L):
        return True
    else:
        return False