def freq_palavras(frases):
    """ Função que retorne um dicionário onde cada palavra
    do mesmo, seja uma chave e tenha como valor o número de
    vezes que ela aparece"""
    dicionario = {}
    lista_palavra = str.split(frases)
    for palavra in lista_palavra:
        if palavra in dicionario:
            dicionario[palavra] = dicionario[palavra] + 1
        else:
            dicionario[palavra] = 1
    return dicionario