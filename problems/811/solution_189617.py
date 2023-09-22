def colchao(medidas,H,L):
    '''
    Função que diz se o colchão de dimensões das medidas
    AxBxC em cm (com A, B e C dentro da lista "medidas" e em ordem
    crescente) passará na porta de altura H em cm e largura L em cm
    list, int, int -> boolean
    '''
    alturaC=medidas[0]
    larguraC=medidas[1]
    comprimentoC=medidas[2]
    
    if H>alturaC and L>larguraC:
        return True
    else:
        return False