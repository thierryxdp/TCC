def faltante(Lista):
    """A entrada é uma lista, que está no parâmetro, com N
    números inteiros - não repetidos - de 1 a N, porém uma das peças faltará
    e a saída é dizer qual a peça que falta"""
    #list -> int
    
    ListaN = Lista[:]
    ListaN.sort()
    n = Lista[0]
    x = Lista[-1]
    QuantidadePecas= 0
    pecafaltante = 1
    while QuantidadePecas < len(ListaN):
        if 1 not in ListaN:
            return 1
        elif ListaN[QuantidadePecas] == range(ListaN):
            return QuantidadePecas + 1
        else:
            return pecafaltante