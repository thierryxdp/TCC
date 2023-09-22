def colchao(medidas,H,L):
    """ função que calcule se o colchão ira passar pela porta dados a altura H e largura L"""
    if medidas [1] <= H:
        return True
    if medidas  [1] <= L:
        return True 
    else:
        return False# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis