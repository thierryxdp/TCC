def colchao(medidas,H,L):
    """ função definida por colchao para resolver esse problema, onde as medidas é uma lista com os tamanhos inteiros A,B,e C, e H ,são os tamanhos inteiros da altura e largura da porta,respectivamente. list-> int"""
    return (medidas[0]<=L and medidas[1]<=H)or(medidas[0]<=H and medidas[1]<=L)