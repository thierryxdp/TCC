def freq_palavras(frases):
    '''Função que dada uma string, retorna um dicionario onde cada palavra dessa string é uma chave e tem como valor o número de vezes que a palavra aparece: str -> dict'''
    dicionario = {}
    palavras = str.split(frases)
    for palavra in palavras:
        if palavra not in dicionario:
            dicionario[palavra] = 1
        else:
            dicionario[palavra] = dicionario.get(palavra) + 1
    return dicionario