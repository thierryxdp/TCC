def freq_palavras(frases):
    """ função que retorna um dicionario, a quantidade de vezes que uma string aparece é o valor e a string a chave
    str -> dict"""
    dicionario = {}
    palavras = str.split(frases)
    for palavra in palavras:
        if palavra not in dicionario:
            dicionario[palavra] = 1
        else:
            dicionario[palavra] = dicionario.get(palavra) + 1
    return dicionario