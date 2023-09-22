# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas, H, L):
    """Retorna se é possível passar um colchão com as dimenssões dadas pela lista 'l'
    por uma porta de dimenssões 'altura', 'largura';
    list, int, int -> bool"""
    if H >= L:
        if medidas[1] <= H and medidas[0] <= L:
            return True
        else:
            return False
    else:
        if medidas[1] <= L and medidas[0] <= H:
            return True
        else:
            return False