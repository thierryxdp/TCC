# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    """2DO """
    if (medidas[1] <= H) or (medidas[1] <= L):
        return True
    elif (medidas[2] <= H) or (medidas[2] <= L):
        return True
    
    return False