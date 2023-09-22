def analise_passagem_colchao(dados_colchao):
    '''analisa se um colchão com dimensões A, B, C (em cm e em ordem crescente) passa por uma porta de largura (L) e  altura (A). Tais dados estão, respectivamente, na lista dada
    list -> bool'''
    a = dados_colchao[0]
    b = dados_colchao[1]
    c = dados_colchao[2]
    h = dados_colchao[3]
    l = dados_colchao[4]

    return (b <= l and a <= h) or (a <= l and c <= h) or (c <= l and b <= h)