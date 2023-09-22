def freq_palavras(string):
    lista=list(string.split(' '))
    [[x, lista.count(x)] for x in set(lista)]
    return dict((x,lista.count(x)) for x in set(lista))