def passacolchao(colchao, altura_porta, largura_porta):
    """Verifica se um colchão passa em dada porta;
    lista, int, int ->bool"""
    if colchao[1] <= altura_porta or colchao[2] <= altura_porta or colchao[1] <= largura_porta or colchao[2] <= largura_porta:
        return True
    else:
        return False