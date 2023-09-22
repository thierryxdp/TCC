def colchao(medidas,H,L):
    '''Função que retorna se o colchão passa pela porta, dadas as medidas do colchão e altura(H) e largura (L) da porta.
    list,float,float->bool'''
    alt_colchao,larg_colchao,comp_colchao=medidas
    nao_passa=(alt_colchao>max(H,L)and larg_colchao>max(H,L))or(alt_colchao>max(H,L) and comp_colchao>max(H,L))or(larg_colchao>max(H,L) and comp_colchao>max(H,L))
    return not nao_passa