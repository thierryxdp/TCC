def freq_palavras(frases):
    '''calcule uma funcao que receba uma string e retorne um dicionario
    onde cada palavra dessa string seja uma chave e tenha como valor o numero
    de vezes que a palavra aparece. str-->dict.'''
    dicionario = {}
    frases=str.split(frases)
    for i in range(len(frases)):
        cont = frases.count(frases[i])
        if i < len(frases):
            dicionario[frases[i]] = cont
    return dicionario