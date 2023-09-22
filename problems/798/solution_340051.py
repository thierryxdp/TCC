def freq_palavras(frases):
    '''retorna um dicionario onde cada palavra de uma string dada seja uma chave e o valor de cada chave seja a quantidade de ocorrencias da palavra associada; str -> dict'''
    frases.lower()
    lista = frases.split(' ',len(frases))
    dicionario = {}
    for palavra in lista:
        dicionario = dicionario + {palavra,}
        dicionario[palavra] = list.count(lista,palavra)
    return dicionario