def analise_passagem_colchao(dados_colchao):
    '''calcula se um colchão com dimensões A, B, C em uma lista crescente (em cm) passa por uma porta de largura (L) e  altura (A)
    list -> bool'''
    a = dados_colchao[0][0]
    b = dados_colchao[0][1]
    c = dados_colchao[0][2]
    h = dados_colchao[1]
    l = dados_colchao[2]

    return (b <= l and a <= h) or (a <= l and b <= h) or (c <= l and a <= h)