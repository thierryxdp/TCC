def freq_palavras(frases):
    '''Recebe uma string e retorna um dicionário em que
    cada palavra dessa string é uma chave e a sua
    frequência na string é o seu valor
    str -> dict'''
    dict = {}
    palavras = frases.split()
    i = 0
    for x in range (0, len(palavras) + 1):
        dict = [palavras[i]] = palavras.count(i)
        i += 1
    return dict