def bolos(A,B,C):
    """Função que calcula e retorna a quantidade total de bolos que
podem ser produzidos de acordo com as quantias necessárias de cada 
ingrediente, dadas as quatidades de ingredientes disponíveis (A xícaras de farinha,
B ovos e C colheres de leite)"""
    return min((int(A/2)),(int(B/3)),(int(c/5)))