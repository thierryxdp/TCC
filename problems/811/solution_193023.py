def colchao(medidas,H,L):
'''Analiza se a segunda maior medida do colchão é menor
que a maior medida da porta e se a menor medida do colchão
é menor que a base. Caso o colchão consiga passar pela porta,
retorna True e caso não, retorna False'''
    a = medidas[0]
    b = medidas[1]
    c = medidas[2]
    if H >= L:
        altura = H
        base = L
    else:
        altura = L
        base = H

    if b <= altura and a <= base:
        return True
    else:
        return False