def colchao(medidas, H, L):
    """Recebe uma lista contendo as três dimensões de um
    colchão e dois números inteiros que são as dimensões
    de uma porta a qual o colchão deve atravessar. A função
    compara as dimensões do colchão com as dimensões da
    porta em 6 posições diferentes (faces paralelas ao
    chão) e retorna True, caso em pelo menos uma delas o
    colchão consiga atravessar ou retorna False caso
    não passe em nenhuma.
    list, int, int -> bool
"""
    A, B, C = medidas
    if H>=A and L>=B or H>=B and L>=A or H>=C and L>=B or H>=B and L>=C or H>=A and L>=C or H>=C and L>=A:
        return True
    else:
        return False