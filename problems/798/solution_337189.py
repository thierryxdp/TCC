def freq_palavras(frase):
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
    counter = 0
    for i in listaPalavras:
        dictFreqPalavras[listaPalavras[counter]]=list.count(listaPalavras,listaPalavras[counter])
    counter += 1
    return dictFreqPalavras