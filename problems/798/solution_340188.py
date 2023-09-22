def freq_palavras(frases):
    '''Recebe uma frase e retorna, em forma de dicionário, as palavras
    e suas respectivas frequências (str -> dict).'''
    dicionario = {}
    palavras = frases.split()
    for palavra in palavras:
        indice = palavras.count(palavra)
        dicionario[palavra] = indice
    return dicionario