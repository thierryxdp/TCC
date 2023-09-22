def freq_palavras(frases):
    ''' Recebe uma string e retorna um dicionário com a contagem de cada palavra'''
    frases = frases.split()
    n = [(i, frases.count(i) for i in frases]
    return dict(n)