def freq_palavras(frases):
    '''Funcao que recebe uma string de entrada (frases) e retorna um dicionario onde as palavras da string são as chaves, e seus valores sao o numero de vezes em que elas aparecem; str -> dict {str:int, str:int,...}'''
    dicionario={}
    for palavra in frases:
        dicionario[palavra]= str.count(frases,palavra)
    return dicionario