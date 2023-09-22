def freq_palavras(frases):
    '''recebe uma string e retorna um dicionário em que
    cada palavra da mesma seja uma chave com o número de
    vezes que a palavra aparece
    string -> dict'''
    dicionario = {}
    frases = frases.split()
    for i in range(len(frases)):
        dicionario[frases[i]] = frases.count(frases[i])
    return dicionario