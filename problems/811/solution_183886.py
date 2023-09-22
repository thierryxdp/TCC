def colchao(medidas,H,L):
    '''Funcao que retorna um dado booleano
    True se o colchao passa pelas portas e
    False caso o contrario, dados os valores
    das medidas do colchao (medidas - A, B e C)
    , da altura da porta (H) e largura da porta (L).
    Dados de entrada: list, int, int
    Valor de saida: bool
    '''
    if medidas[0]<L and medidas[1]<H:
        return True
    elif medidas[1]<L and medidas[0]<H:
        return not False