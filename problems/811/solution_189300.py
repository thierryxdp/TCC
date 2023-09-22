def colchao(medidas,H,L):
    ''' Dada uma lista com as medidas do colchão e H e L altura
    e largura respectivas da porta, a função retorna uma booleana
    dizendo se o colchão passa ou não na porta.
    list, int, int -> bool'''
    J = medidas[1]

    if H >= J or L >= J:
        t = True
    else:
        t = False
    return t