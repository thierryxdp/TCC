# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas, H, L):
    """Retorna se o colchão passa ou não pela porta.
    list, int, int -> bool"""
    if (medidas[0] > H and medidas[1] > L) or (medidas[1] > H and medidas[0] > L):
        return False
    return True