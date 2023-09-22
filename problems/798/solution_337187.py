def freq_palavras(frases):
    '''retorna um dicionario com as palavras da entrada frase e seu valores
    relacionados as suas frequencias
    str->dict'''
    a = frase
    a = str.replace(a,'-',' ')
    a = str.replace(a,',',' ')
    a = str.replace(a,'...',' ')
    a = str.replace(a,':',' ')
    a = str.replace(a,'.',' ')
    a = str.replace(a,';',' ')
    a = str.replace(a,'!',' ')
    a = str.replace(a,'?',' ')
    listaPalavras = str.split(a)
    dictFreqPalavras = {}
    for i in listaPalavras:
        dictFreqPalavras[listaPalavras[i]]=list.count(listaPalavras,listaPalavras[i])
    return dictFreqPalavras