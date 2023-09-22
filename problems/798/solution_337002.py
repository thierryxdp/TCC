def freq_palavras(frases):
    '''Função que recebe uma string e retorna um dicionário onde cada palavra dessa string seja uma chave que tem como valor o número de vezes que a palavra aparece.
    str -> dict'''
    palavras = str.split(frases)
    dicionario = {}
    for i in palavras:
        if i not in dicionario:
            dicionario[i] = 1
        else:
            dicionario[i] = dict.get(dicionario, i) + 1
    return dicionario