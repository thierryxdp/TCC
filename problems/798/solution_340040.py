def freq_palavras(frases):
    '''Função retorna a quantidade de vezes que uma palavra se repetiu
    str-->dic'''
    a = frases.split(' ')
    d = {}
    for i in a:
        d[i]=a.count(i)
    return d