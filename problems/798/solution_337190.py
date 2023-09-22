def freq_palavras(frases):
    '''retorna um dicionario com as palavras da entrada frase e seu valores
    relacionados as suas frequencias
    str->dict'''
    listaPalavras = str.split(frases)
    dictFreqPalavras = {}
    counter = 0
    for i in listaPalavras:
        dictFreqPalavras[listaPalavras[counter]]=list.count(listaPalavras,listaPalavras[counter])
    counter += 1
    return dictFreqPalavras