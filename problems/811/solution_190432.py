def colchao(medidas,H,L):
    '''entrada é o tamanho do 
    colchao em centimentros,da menor para a maior.
    dando o resultado se o colchão passa na porta ou nao
    ent-int
    saida-bool
    '''
    A,B,C= medidas
    return min(B,C)<=max(H,L)