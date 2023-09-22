# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas, H, L):
    """Retorna se o colchão passa ou não pela porta.
    list, int, int -> bool"""
    if (medidas[0] > H or medidas[1] > L) and (medidas[1] > H or medidas[0] > L):
        return False
    return True