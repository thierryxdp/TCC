def freq_palavras(frases):
    '''Recebe uma string e retorna um dicionário com cada
    palavra sendo uma chave e seu valor atribuido será a
    quantidade de vezes que a palavra aparece na string.
    str -> dict'''
    lista_palavras = str.split(frases, ' ')
    dicionario = {}
    for palavra in lista_palavras:
        if palavra in dicionario:
            dicionario[palavra] += 1
        else:
            dicionario[palavra] = 1
    return dicionario