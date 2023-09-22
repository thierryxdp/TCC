def colchao(medidas,H,L):
    '''Funcao que retorna um dado booleano:
    True se o colchao passa pelas portas e
    False caso o contrario, dados os valores
    das medidas do colchao: largura do colchao (Lc);
    altura do colchao (Hc); comprimento do colchao (Cc);
    , da altura da porta (H) e largura da porta (L).
    Dados de entrada: list, int, int
    Valor de saida: bool
    '''
    if medidas[2]<=H and medidas[1]<=L:
        return True
    if medidas[1]<=H and medidas[0]<=L:
        return True
    else:
        return False