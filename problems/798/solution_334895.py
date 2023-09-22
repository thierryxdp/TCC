def freq_palavras(frases):
    """função que retorna o número de vezes que uma palavra é repetida numa frase
    str -> dict"""
    dicionario = {}
    lista = str.split(frases,' ')
    for palavra in lista:
        dicionario[palavra]= lista.count(palavra)
    return dicionario