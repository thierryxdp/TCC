def colchao (dimensao, H, L):
    '''calcula se o colchao novo passsa ou não na porta de acordo
    com o tamanho e largura da porta
    [int, int, int], int, int -> bool'''
    porta = [H, L]
    if dimensao[1] > porta[0] and dimensao[1] > porta[1]:
        return False
    else:
        return True