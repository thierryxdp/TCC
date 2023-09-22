def analise_passagem_colchao(dimensoes_colchao, h, l):
    '''calcula se um colchão com dimensões A, B, C em uma lista crescente (em cm) passa por uma porta de largura (l) e  altura (a)
    list -> bool'''
    a = dimensoes_colchao[1]
    b = dimensoes_colchao[2]
    c = dimensoes_colchao[0]

    return (b <= l and c <= h) or (a <= l and c <= h) or (c <= l and a <= h)