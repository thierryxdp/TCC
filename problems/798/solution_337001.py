def freq_palavras(frases):
    '''Função que recebe uma frase e retorna um dicionário com a quantidade de vezes que as
    palavras aparecem
    str -> dict'''
    palavras = str.split(frases)
    dicionario = {}
    for i in palavras:
        if i not in dicionario:
            dicionario[i] = 1
        else:
            dicionario[i] = dict.get(dicionario, i) + 1
    return dicionario