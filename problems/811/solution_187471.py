# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
    """Função que retorna se o colchão passa pela porta
    dado as medidas do colchão.
    list, float, float--> bool"""
    
def colchao(medidas, H, L):
    
    if medidas[1] <= H:
        return True
    if medidas[1] <= L:
        return True
    if medidas[2] <= H:
        return True
    if medidas[2] <= L:
        return True
    else:
        return False