def freq_palavras(frases):
    '''Retorna um dicionario com o nome da palavra e quantas vezes ela repete;
    str->dict'''
    palavras=frases.split()
    dicionario={}
    i=0
    for i in range(len(palavras)):
        dicionario[palavras[i]]=palavras.count(palavras[i])
        i+=1
    return dicionario