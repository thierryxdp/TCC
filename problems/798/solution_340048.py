def freq_palavras(frases):
    '''retorna um dicionario onde cada palavra de uma string dada seja uma chave e o valor de cada chave seja a quantidade de ocorrencias da palavra associada; str -> dict'''
    frases.lower()
    lista = frases.split(' ',len(frases))
    dicionario = {}
    i = 0
    while i<=len(lista):
        dicionario = dicionario + {lista[i]:list.count(lista,lista[i]),}
        i = i + 1
    return dicionario