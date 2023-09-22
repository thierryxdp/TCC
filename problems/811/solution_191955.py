# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    """Verifica se um colchao com tamnha da tupla medidas
    é capaz de passar por um porata de altura H e largura L
    tupla[3], int, int --> bool"""
    
    if (medidas[1] <= H) or (medidas[1] <= L):
        # Verifica se medida 1 pode passar pela porta
        return True
    elif (medidas[2] <= H) or (medidas[2] <= L):
        # Verifica se medida 2 pode passar pela porta
        return True
    
    return False