def freq_palavras(frases):
    '''Recebe uma string e retorna um dicionário em que
    cada palavra dessa string é uma chave e a sua
    frequência na string é o seu valor
    str -> dict'''
    dict = {}
    palavras = frases.split()
    for i in range(0, len(palavras)):
        dict[palavras[i]] = palavras.count(palavras[i])
    return dict