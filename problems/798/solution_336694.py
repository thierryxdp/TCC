def freq_palavras(frase):
    ''' relaciona o número de vezes que uma string aparece com a string
    em questão em uma forma de dicionnário, onde as strings são as chaves;
    str->dict'''
    dicionario={}
    for frase in frase:
        if frase not in dicionario:
            dicionario(frase)=1
        else:
            dicionario(frase)+=1
    return dicionario