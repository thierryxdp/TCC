def freq_palavras(frase):
    '''Retorna um dicionario com as palavras e
    suas respectivas repeticoes em uma string
    str --> dict'''
    qntd = {}
    frase = str.split(frase)
    for i in frase:
        if i in qntd:
            qntd[i] = qntd[i]+1
        else:
            qntd[i] = 1
    return qntd