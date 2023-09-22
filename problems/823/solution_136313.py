def faltante(Lista):
    """A entrada é uma lista, que está no parâmetro, com N
    números inteiros - não repetidos - de 1 a N, porém uma das peças faltará
    e a saída é dizer qual a peça que falta"""
    #list -> int
    
    ListaN = Lista[:]
    ListaN.sort()
    QuantidadePecas= 0
    pecafaltante = 1
    while QuantidadePecas < len(ListaN):
        if ListaN[QuantidadePecas] == QuantidadedePecas + 1:
            QuantidadedePecas += 1
        else:
            Pecas = QuantidadePecas + 1