def freq_palavras(frases):
    '''Retorna um dicionario onde cada palavra dessa string seja uma chave e tenha como valor o numero de vezes que a palavra aparece dado uma string
    string -> dict'''
    dicionario = {}
    frases = frases.split()
    for i in range(len(frases)):
        dicionario[frases[i]] = frases.count(frases[i])
    return dicionario