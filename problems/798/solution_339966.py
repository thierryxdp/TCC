def freq_palavras(frases):
    '''Funcao que contabiliza as palavras dada nas frases.
    Str->dict'''
    s = frases.split()
    dicionario = {}
    for palavra in s:
        cont = s.count(palavra)
        if cont == 1:
            dicionario.update({palavra: 1})
        if cont>1:
            dicionario.update({palavra: cont})
    return dicionario