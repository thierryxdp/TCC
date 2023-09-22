def freq_palavras(frases):
    '''Função que recebe uma string e retorna um dicionário com a quantidade de cada palavra.'''
    '''str->dict'''
    d = {}
    string = str.split(frases)
    for string in string:
        if string not in d:
            d[string] = 1
        else:
            d[string] = d.get(string)+1
    return d