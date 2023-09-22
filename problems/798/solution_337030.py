def freq_palavras(frases):
    '''
    função que recebe uma string e retorna um dicionário
    onde cada palavra dessa string é uma chave e tem como valor
    o número de vezes que a palavra aparece
    str -> dict
    '''
    
    dicionario={}
    for palavra in frases:
        if palavra in frases:
            dicionario[palavra] = frases.count(palavra)
    return dicionario