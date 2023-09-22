def freq_palavras(frases):
    '''Funcao que recebe uma string de entrada (frases) e retorna um dicionario onde as palavras da string são as chaves, e seus valores sao o numero de vezes em que elas aparecem; str -> dict {str:int, str:int,...}'''
    dicionario={}
    lista=str.split(frases)
    for palavra in lista:
        dicionario[palavra]= str.count(lista,palavra)
    return dicionario