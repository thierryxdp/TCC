def colchao(dimensoesColchao,H,L):
    '''essa funcao retorna true se o colchao comprado passa na porta e false se nao passa '''
    largura = dimensoesColchao[1]
    altura = dimensoesColchao[2]
    # A = profundidade B = largura C = Altura
    if largura > H:
        return False
    else:
        return True