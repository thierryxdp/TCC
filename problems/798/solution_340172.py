def freq_palavras(frases):
    '''Função que retorna um dicionario com a palavra e quantas vezes ela se repete na frase'''
    liston = frases.split()
    dicioboy = {}
    for palavra in liston:
        chabe = liston.count(palavra)
        dicioboy[palavra] = chabe
    return dicioboy