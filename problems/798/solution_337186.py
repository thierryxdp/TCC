def freq_palavras(frases):
    '''retorna um dicionario com as palavras da entrada frase e seu valores
    relacionados as suas frequencias
    str->dict'''
    listaPalavras = str.split(frases)
    dictFreqPalavras = {}
    for i in listaPalavras:
        dictFreqPalavras[listaPalavras[i]]=list.count(listaPalavras,listaPalavras[i])
    return dictFreqPalavras