def freq_palavras(frases):
    '''Função que calcula e retorna um dicionário com a quantidade de cada palavra. str->dict'''
    dicionario = {}
    p = str.split(frases)
    for string in p:
        if p not in dicionario:
            dicionario[p] = 1
        else:
            dicionario[p] = dicionario.get(p)+1
    return dicionario