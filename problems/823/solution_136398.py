def faltante(Lista):
    """A entrada é uma lista, que está no parâmetro, com N
    números inteiros - não repetidos - de 1 a N, porém uma das peças faltará
    e a saída é dizer qual a peça que falta"""
    #list -> int
    
    ListaN = Lista[:]
    ListaN.sort()
    n = 1
    QuantidadePecas= 0
    pecafaltante = 1
    while n < len(ListaN):
        if ListaN[n-1] = 1:
            return 1
        ListaN + 1
        elif ListaN[QuantidadePecas] == range(ListaN):
            return QuantidadePecas + 1
        else:
            return pecafaltante