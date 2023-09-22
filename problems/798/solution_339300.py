def freq_palavras(frases):
    '''Função que recebe uma string e retorne um dicionario
    onde cada palavra dessa string seja uma chave e tenha 
    como valor o numero de vezes que a palavra aparece
    str -> dic'''
    d = dict()
    frases1 = str.split(frases,' ')
    for i in frases1:         
        if i not in d:
            d[i] = 0
        if i in d:
            d[i] += 1
    return d