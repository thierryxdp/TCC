def freq_palavras(frase):
    ''' relaciona o número de vezes que uma string aparece com a string
    em questão em uma forma de dicionnário, onde as strings são as chaves;
    str->dict'''
    dicionario={}
    for string in frase:
        if string not in dicionario:
            dicionario(string)=1
        else:
            dicionario(string)+=1
    return dicionario