def freq_palavras(f):
    '''Retorna um dicionário com quantas vezes uma palavra
    apareceu na frase.
    str -> dict'''
    dic = {}
    for p in len(str.split(f, ' ')):
        if p in dic:
            dic[p] += 1
        else:
            dic[p] = 1
    return dic