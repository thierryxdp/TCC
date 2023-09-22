def posLetra(string, letra, numero):
    """A Entrada serão os três elementos indicados no parâmetro
    sendo que o número indicará a ocorrência da letra. O Retorno
    é a posição da string em relação a posição da letra, que caso
    seja inferior a quantidade de ocorrencia do que fora pedido
   , deve-se aplicar o - 1"""
    #str, str, int --> int
    indice = 0
    QuantidadeOcorrencias = 0
    while indice < len(string):
        if string[indice] == letra:
            indice + 1
        if QuantidadeOcorrencias == numero:
            return QuantidadeOcorrencias
        return - 1