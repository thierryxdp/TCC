def freq_palavras(frases):
    '''Retorna um dicionario com o nome da palavra e quantas vezes ela repete;
    str->dict'''
    palavras=frases.split()
    dicionario={}
    for i in range(len(palavras)):
        dicionario[palavras[i]]=palavras.count(palavras[i])
    return dicionario